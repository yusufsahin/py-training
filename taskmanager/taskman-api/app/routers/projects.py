from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.deps import get_current_user
from app.models import Profile, Project
from app.schemas.project import ProjectCreate, ProjectResponse

router = APIRouter(prefix="/projects", tags=["projects"])


@router.get("", response_model=list[ProjectResponse])
def list_projects(
    db: Session = Depends(get_db),
    current: Profile = Depends(get_current_user),
) -> list[Project]:
    return (
        db.query(Project)
        .filter(Project.owner_id == current.id)
        .order_by(Project.created_at.desc())
        .all()
    )


@router.post("", response_model=ProjectResponse, status_code=status.HTTP_201_CREATED)
def create_project(
    body: ProjectCreate,
    db: Session = Depends(get_db),
    current: Profile = Depends(get_current_user),
) -> Project:
    project = Project(name=body.name.strip(), owner_id=current.id)
    db.add(project)
    db.commit()
    db.refresh(project)
    return project


@router.delete("/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_project(
    project_id: UUID,
    db: Session = Depends(get_db),
    current: Profile = Depends(get_current_user),
) -> None:
    project = db.query(Project).filter(Project.id == project_id, Project.owner_id == current.id).first()
    if project is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")
    db.delete(project)
    db.commit()
