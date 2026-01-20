from datetime import datetime, timedelta
from typing import Optional
from jose import jwt
from app.core.config import settings

ALGORITHM = "HS256"

def create_access_token(
    data: dict, 
    expires_delta: Optional[timedelta] = None) -> str:
    """
    Creates a signed JWT access token.

    - data: must include {"sub": "<user_id>"}
    - expires_delta: optional custom expiration time
    """

    to_encode = data.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.access_token_expire_minutes
        )
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(
        to_encode,
        settings.secret_key,
        algorithm=ALGORITHM
    )

    return encoded_jwt

def decode_access_token(token: str) -> dict:
    try:
        payload = jwt.decode(
            token,
            settings.secret_key,
            algorithms=[ALGORITHM]
        )
        return payload
    except JWTError:
        return {}
