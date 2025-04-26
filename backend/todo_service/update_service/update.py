from fastapi import APIRouter, Depends, Header, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Todo
from schemas import TodoUpdate, TodoInDB
from utils import decode_token

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.put("/todos/{todo_id}", response_model=TodoInDB)
def update_todo(todo_id: int, todo: TodoUpdate, Authorization: str = Header(...), db: Session = Depends(get_db)):
    username = decode_token(Authorization.replace("Bearer ", ""))
    db_todo = db.query(Todo).filter_by(id=todo_id, username=username).first()
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    db_todo.title = todo.title
    db_todo.completed = todo.completed
    db.commit()
    db.refresh(db_todo)
    return db_todo
