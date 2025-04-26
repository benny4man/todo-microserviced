from fastapi import APIRouter, Depends, Header
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Todo
from utils import decode_token

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.delete("/todos", status_code=204)
def clear_completed(Authorization: str = Header(...), db: Session = Depends(get_db)):
    username = decode_token(Authorization.replace("Bearer ", ""))
    db.query(Todo).filter_by(username=username, completed=True).delete()
    db.commit()
