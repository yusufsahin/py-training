from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field


class TaskCreate(BaseModel):
    project_id: UUID
    title: str = Field(min_length=1, max_length=500)
    description: str | None = None
    status: str = "todo"
    priority: str = "medium"
    due_date: datetime | None = None
    position: float = 0.0
    label_ids: list[UUID] | None = None


class TaskUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=500)
    description: str | None = None
    status: str | None = None
    priority: str | None = None
    due_date: datetime | None = None
    position: float | None = None
    is_deleted: bool | None = None
    label_ids: list[UUID] | None = None


class LabelBrief(BaseModel):
    id: UUID
    name: str
    color: str

    model_config = {"from_attributes": True}


class TaskResponse(BaseModel):
    id: UUID
    project_id: UUID
    title: str
    description: str | None
    status: str
    priority: str
    due_date: datetime | None
    position: float
    is_deleted: bool
    created_at: datetime
    labels: list[LabelBrief]

    model_config = {"from_attributes": True}
