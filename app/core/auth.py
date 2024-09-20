from fastapi import HTTPException, Security
from fastapi.security import api_key
from app.core.config import Config

api_key_header = api_key.APIKeyHeader(name="X-API-KEY")

async def validate_api_key(key: str = Security(api_key_header)):
    if key != Config.X_API_KEY:
        raise HTTPException(
    status_code=401, detail=f"Unauthorized - Invalid API Key"
)

    return None
