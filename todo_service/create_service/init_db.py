from database import engine, Base
from models import Todo

Base.metadata.create_all(bind=engine)