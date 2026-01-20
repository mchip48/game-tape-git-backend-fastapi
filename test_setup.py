# backend/test_setup.py

from app.core.config import settings
from app.services.security import hash_password, verify_password
from app.services.jwt import create_access_token
from datetime import timedelta

print("=== CONFIG TEST ===")
print("App Name:", settings.app_name)
print("Environment:", settings.env)
print("Database URL:", settings.database_url)
print("Redis URL:", settings.redis_url)
print("Secret Key Exists:", bool(settings.secret_key))

print("\n=== PASSWORD HASH TEST ===")
plain_password = "mysecret123"
hashed_password = hash_password(plain_password)
print("Hashed password:", hashed_password)
print("Verify correct password:", verify_password("mysecret123", hashed_password))
print("Verify wrong password:", verify_password("wrongpass", hashed_password))

print("\n=== JWT TEST ===")
token_data = {"sub": "user123"}
access_token = create_access_token(token_data)
print("Generated JWT:", access_token)
