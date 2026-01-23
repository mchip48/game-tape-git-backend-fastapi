# app/core/security.py

import os
from fastapi import Header, HTTPException

async def verify_api_key(x_api_key: str = Header(None)):
    api_key = os.getenv("API_KEY")

    if not api_key:
        raise HTTPException(
            status_code=500,
            detail="Server misconfiguration: API_KEY not set"
        )

    if x_api_key != api_key:
        raise HTTPException(
            status_code=401,
            detail="Invalid or missing API key"
        )

    return True
