from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.repository.db import get_db
from src.models.user import User
from src.api.auth import admin_only

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.get("/users")
def get_all_users(
    db: Session = Depends(get_db),
    admin: User = Depends(admin_only)
):
    return db.query(User).all()
