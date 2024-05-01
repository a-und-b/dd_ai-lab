from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from hashlib import sha256

Base = declarative_base()

class Job(Base):
    __tablename__ = 'jobs'
    id = Column(String, primary_key=True, default=lambda context: generate_job_id(context.get_current_parameters()['nickname']))
    job_number = Column(Integer, unique=True)  # Fortlaufende Nummer jedes Jobs
    nickname = Column(String)
    character = Column(String)  # Name des Charakters
    fandom = Column(String)  # Zugehöriger Fandom, z.B. "Star Trek TNG"
    background = Column(Text)  # Hintergrundgeschichte oder -szenario
    mood = Column(String)  # Stimmung, z.B. "heroisch", "verträumt"
    style = Column(String)  # Stil, z.B. "realistisch", "Anime/Manga"
    status = Column(String, default='new')  # Der aktuelle Status des Jobs
    created_at = Column(DateTime, default=datetime.utcnow)  # Erstellungszeitpunkt
    updated_at = Column(DateTime, default=datetime.utcnow)  # Zeitpunkt der letzten Aktualisierung des Jobs
    job_url = Column(String, default=lambda context: f"https://andersundbesser.de/lfg/{context.get_current_parameters()['id']}")  # URL zum Job

engine = create_engine('sqlite:///cosplay.db', echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
