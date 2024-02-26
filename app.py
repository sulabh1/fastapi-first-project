from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import  Session

from models.todo import Todo
from db_session.db import get_db





class Todos(BaseModel):
	name:str
	description: str = None

app = FastAPI()



@app.post("/")
async def create_root(todo:Todos, db:Session = Depends(get_db)):
	print(todo, ">>>>>>>>>>>>>>>>>>")
	db_item = Todo(name=todo.name, description=todo.description)
	db.add(db_item)
	db.commit()
	db.refresh(db_item)
	return db_item
	
@app.get("/")
async def get_root(todo:Todos, db:Session = Depends(get_db)):
	item = db.query(Todo).all()
	return item