from fastapi import APIRouter, Depends, Header
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Todo
from schemas import TodoCreate, TodoInDB
from utils import decode_token

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/todos", response_model=TodoInDB)
def create_todo(todo: TodoCreate, Authorization: str = Header(...), db: Session = Depends(get_db)):
    username = decode_token(Authorization.replace("Bearer ", ""))
    new_todo = Todo(title=todo.title, completed=todo.completed, username=username)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo
