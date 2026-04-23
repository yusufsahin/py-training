from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.deps import get_current_user
from app.models import Label, Profile
from app.schemas.auth import ProfileResponse, TokenResponse, UserLogin, UserRegister
from app.security import create_access_token, hash_password, verify_password

router = APIRouter(prefix="/auth", tags=["auth"])

DEFAULT_LABELS: list[tuple[str, str]] = [
    ("Frontend", "#3b82f6"),
    ("Backend", "#10b981"),
    ("Bug", "#ef4444"),
    ("Feature", "#8b5cf6"),
    ("Design", "#f59e0b"),
]


@router.post("/register", response_model=TokenResponse)
def register(body: UserRegister, db: Session = Depends(get_db)) -> TokenResponse:
    if db.query(Profile).filter(Profile.email == body.email.lower()).first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    profile = Profile(
        email=body.email.lower(),
        hashed_password=hash_password(body.password),
        full_name=body.full_name,
        avatar_url=None,
    )
    db.add(profile)
    db.flush()
    for name, color in DEFAULT_LABELS:
        db.add(Label(owner_id=profile.id, name=name, color=color))
    db.commit()
    db.refresh(profile)
    token = create_access_token(profile.id)
    return TokenResponse(access_token=token)


@router.post("/login", response_model=TokenResponse)
def login(body: UserLogin, db: Session = Depends(get_db)) -> TokenResponse:
    profile = db.query(Profile).filter(Profile.email == body.email.lower()).first()
    if profile is None or not verify_password(body.password, profile.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password")
    token = create_access_token(profile.id)
    return TokenResponse(access_token=token)


@router.get("/me", response_model=ProfileResponse)
def me(current: Profile = Depends(get_current_user)) -> ProfileResponse:
    return ProfileResponse.model_validate(current)
