# app/core/security.py

import os
from fastapi import Header, HTTPException, status

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise RuntimeError("API_KEY not set in environment")


async def verify_api_key(x_api_key: str = Header(...)):
    """
    Dependency that verifies the API key sent in request headers.
    Client must send: X-API-Key: <your_key>
    """
    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API key",
        )
