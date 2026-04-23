from uuid import UUID

from pydantic import BaseModel


class LabelResponse(BaseModel):
    id: UUID
    name: str
    color: str

    model_config = {"from_attributes": True}
