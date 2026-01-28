from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserResponse, PasswordChange
from app.services.deps import get_current_user, get_db
from app.services.security import verify_password, hash_password

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get("/me", response_model=UserResponse)
def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

@router.post("/change-password")
def change_password(
    passwords: PasswordChange,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if not verify_password(passwords.old_password, current_user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect current password"
        )

    # Update password safely
    current_user.hashed_password = hash_password(passwords.new_password)
    db.commit()  # no add(), already attached to session

    return {"message": "Password successfully updated!"}
