from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from hashlib import sha256

Base = declarative_base()

def generate_job_id(nickname):
    timestamp = int(datetime.utcnow().timestamp())
    nickname_hash = sha256(nickname.encode()).hexdigest()[:8]  # Kurzer Hash des Nicknames
    return f"{timestamp}{nickname_hash}"

class Job(Base):
    __tablename__ = 'jobs'
    id = Column(String, primary_key=True, default=lambda context: generate_job_id(context.get_current_parameters()['nickname']))
    nickname = Column(String)
    status = Column(String, default='new')
    created_at = Column(DateTime, default=datetime.utcnow)
    job_url = Column(String, default=lambda context: f"https://andersundbesser.de/lfg/{context.get_current_parameters()['id']}")

engine = create_engine('sqlite:///cosplay.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
