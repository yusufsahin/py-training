from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session, joinedload

from app.database import get_db
from app.deps import get_current_user
from app.models import Label, Profile, Project, Task
from app.models import TaskPriority, TaskStatus
from app.schemas.task import TaskCreate, TaskResponse, TaskUpdate

router = APIRouter(prefix="/tasks", tags=["tasks"])


def _validate_status(value: str) -> str:
    allowed = {e.value for e in TaskStatus}
    if value not in allowed:
        raise HTTPException(status_code=400, detail=f"Invalid status: {value}")
    return value


def _validate_priority(value: str) -> str:
    allowed = {e.value for e in TaskPriority}
    if value not in allowed:
        raise HTTPException(status_code=400, detail=f"Invalid priority: {value}")
    return value


def _sync_labels(db: Session, task: Task, owner_id: UUID, label_ids: list[UUID] | None) -> None:
    if label_ids is None:
        return
    unique = list(dict.fromkeys(label_ids))
    if not unique:
        task.labels = []
        return
    labels = db.query(Label).filter(Label.owner_id == owner_id, Label.id.in_(unique)).all()
    if len(labels) != len(unique):
        raise HTTPException(status_code=400, detail="One or more labels are invalid")
    task.labels = labels


def _task_query(db: Session, current: Profile):
    return (
        db.query(Task)
        .join(Project)
        .options(joinedload(Task.labels))
        .filter(Project.owner_id == current.id)
    )


@router.get("", response_model=list[TaskResponse])
def list_tasks(
    project_id: UUID = Query(...),
    db: Session = Depends(get_db),
    current: Profile = Depends(get_current_user),
) -> list[Task]:
    project = db.query(Project).filter(Project.id == project_id, Project.owner_id == current.id).first()
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return (
        _task_query(db, current)
        .filter(Task.project_id == project_id, Task.is_deleted.is_(False))
        .order_by(Task.position, Task.created_at)
        .all()
    )


@router.post("", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(
    body: TaskCreate,
    db: Session = Depends(get_db),
    current: Profile = Depends(get_current_user),
) -> Task:
    project = db.query(Project).filter(Project.id == body.project_id, Project.owner_id == current.id).first()
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    task = Task(
        project_id=body.project_id,
        title=body.title.strip(),
        description=body.description,
        status=_validate_status(body.status),
        priority=_validate_priority(body.priority),
        due_date=body.due_date,
        position=body.position,
        is_deleted=False,
    )
    db.add(task)
    db.flush()
    _sync_labels(db, task, current.id, body.label_ids)
    db.commit()
    db.refresh(task)
    task = _task_query(db, current).filter(Task.id == task.id).first()
    assert task is not None
    return task


@router.patch("/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: UUID,
    body: TaskUpdate,
    db: Session = Depends(get_db),
    current: Profile = Depends(get_current_user),
) -> Task:
    task = _task_query(db, current).filter(Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    data = body.model_dump(exclude_unset=True)
    label_ids = data.pop("label_ids", None)
    if "title" in data and data["title"] is not None:
        data["title"] = data["title"].strip()
    if "status" in data and data["status"] is not None:
        data["status"] = _validate_status(data["status"])
    if "priority" in data and data["priority"] is not None:
        data["priority"] = _validate_priority(data["priority"])
    for key, value in data.items():
        setattr(task, key, value)
    _sync_labels(db, task, current.id, label_ids)
    db.commit()
    task = _task_query(db, current).filter(Task.id == task_id).first()
    assert task is not None
    return task
