from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.user import User
from app.services.security import hash_password, verify_password
from app.services.jwt import create_access_token
from app.schemas.user import UserCreate, UserResponse
from app.core.config import settings
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Register Endpoint - Post Request

@router.post("/register", response_model=UserResponse)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    # Checks if user already exists
    existing_user = db.query(User).filter(User.email == user_in.email).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    
    # Hashes password
    hashed_pw = hash_password(user_in.password)

    # Create User Object
    new_user = User(username=user_in.username, email=user_in.email, hashed_password=hashed_pw)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # return {"message": "User successfully created!", "user_id": new_user.id}
    return new_user



# Login Endpoint - Post Request

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # Finds user
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid credentials")
    
    # Verifies password
    if not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid credentials")
    
    # Creates JWT
    token = create_access_token({"sub": str(user.id)})

    return {"access_token": token, "token_type": "bearer"}

