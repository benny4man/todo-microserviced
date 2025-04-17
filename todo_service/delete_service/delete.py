from fastapi import APIRouter, Depends, Header, HTTPException
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

@router.delete("/todos/{todo_id}", status_code=204)
def delete_todo(todo_id: int, Authorization: str = Header(...), db: Session = Depends(get_db)):
    username = decode_token(Authorization.replace("Bearer ", ""))
    db_todo = db.query(Todo).filter_by(id=todo_id, username=username).first()
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(db_todo)
    db.commit()
