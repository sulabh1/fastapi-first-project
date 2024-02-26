from db_session.db_connect import db_connect

def get_db():
	db = db_connect()["db"]

	try:
		yield db
		
	finally:
		db.close()