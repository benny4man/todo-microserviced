from fastapi import APIRouter, Depends, Header
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Todo
from schemas import TodoInDB
from utils import decode_token

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/todos", response_model=list[TodoInDB])
def get_todos(Authorization: str = Header(...), db: Session = Depends(get_db)):
    username = decode_token(Authorization.replace("Bearer ", ""))
    return db.query(Todo).filter_by(username=username).all()
