from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


def db_connect():
	Base = declarative_base()
	connection_string= "postgresql://postgres:password@localhost:5432/testtodo"
	engine = create_engine(connection_string)
	Session_Local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
	db = Session_Local()
	return {
		"base":Base,
		"engine":engine,
		"db":db
	}