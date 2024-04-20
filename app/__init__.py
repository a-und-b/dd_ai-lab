from utils.database import create_database, create_session

engine = create_database()
session = create_session(engine)