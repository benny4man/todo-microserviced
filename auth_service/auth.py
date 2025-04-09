from fastapi import APIRouter, HTTPException, Depends, status, Header
from sqlalchemy.orm import Session
from database import SessionLocal
import models as db_models
from schemas import User as RequestUser, Token
from users_db import pwd_context
from utils import create_access_token, decode_access_token

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/signup")
def signup(user: RequestUser, db: Session = Depends(get_db)):
    existing_user = db.query(db_models.User).filter_by(username=user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    hashed_pw = pwd_context.hash(user.password)
    new_user = db_models.User(username=user.username, hashed_password=hashed_pw)
    db.add(new_user)
    db.commit()
    return {"message": "User created successfully"}

@router.post("/login", response_model=Token)
def login(user: RequestUser, db: Session = Depends(get_db)):
    db_user = db.query(db_models.User).filter_by(username=user.username).first()
    if not db_user or not pwd_context.verify(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}

@router.get("/validate")
def validate_token(Authorization: str = Header(...)):
    if not Authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Authorization header must start with 'Bearer '")

    token = Authorization.replace("Bearer ", "")
    payload = decode_access_token(token)

    if not payload:
        raise HTTPException(status_code=403, detail="Invalid or expired token")

    return {"username": payload.get("sub")}
