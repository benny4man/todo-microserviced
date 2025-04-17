from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import models as db_models
from schemas import User as RequestUser, Token
from users_db import pwd_context
from utils import create_access_token

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/login", response_model=Token)
def login(user: RequestUser, db: Session = Depends(get_db)):
    db_user = db.query(db_models.User).filter_by(username=user.username).first()
    if not db_user or not pwd_context.verify(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}
