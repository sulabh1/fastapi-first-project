from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from db_session.db_connect import db_connect


Base = db_connect()["base"]
engine=db_connect()["engine"]

class Todo(Base):
	__tablename__ = "Todo"

	id=Column(Integer, primary_key=True, index=True)
	name=Column(String)
	description=Column(String)

Base.metadata.create_all(bind=engine)