from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.deps import get_current_user
from app.models import Label, Profile
from app.schemas.label import LabelResponse

router = APIRouter(prefix="/labels", tags=["labels"])


@router.get("", response_model=list[LabelResponse])
def list_labels(
    db: Session = Depends(get_db),
    current: Profile = Depends(get_current_user),
) -> list[Label]:
    return db.query(Label).filter(Label.owner_id == current.id).order_by(Label.name).all()
