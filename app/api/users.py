from app.models.user import User
from app.schemas.user import UserResponse, PasswordChange
from app.services.deps import get_current_user
from app.services.security import verify_password, hash_password
from sqlalchemy.orm import Session
from app.api.auth import get_db

from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

# Current user GET request

@router.get("/me", response_model=UserResponse)
def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

# Change current password

@router.post("/change-password")
def change_password(
    passwords: PasswordChange,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    # Verifies old password
    if not verify_password(passwords.old_password, current_user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect current password"
        )
    
    # Hashes new password
    current_user.hashed_password = hash_password(passwords.new_password)

    # Makes sure SQLAlchemy knows it's updated
    db.add(current_user)

    # Saves to db
    db.commit()

    # Refreshes current instance
    db.refresh(current_user)

    return {"message": "Password successfully updated!"}