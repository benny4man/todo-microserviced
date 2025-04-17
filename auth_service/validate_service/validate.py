from fastapi import APIRouter, HTTPException, Header
from utils import decode_access_token

router = APIRouter()

@router.get("/validate")
def validate_token(Authorization: str = Header(...)):
    if not Authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Authorization header must start with 'Bearer '")
    token = Authorization.replace("Bearer ", "")
    payload = decode_access_token(token)
    if not payload:
        raise HTTPException(status_code=403, detail="Invalid or expired token")
    return {"username": payload.get("sub")}
