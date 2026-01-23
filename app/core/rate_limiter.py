from slowapi import Limiter
from slowapi.util import get_remote_address
import os

def api_key_identifier(request):
    return request.headers.get("X-API-KEY") or get_remote_address(request)

limiter = Limiter(key_func=api_key_identifier)