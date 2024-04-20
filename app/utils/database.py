from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

def create_database():
    engine = create_engine('sqlite:///data/cosplay_photography.db')
    Base.metadata.create_all(engine)
    return engine

def create_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()