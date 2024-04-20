from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Cosplayer(Base):
    __tablename__ = 'cosplayers'

    id = Column(Integer, primary_key=True)
    nickname = Column(String(100), unique=True, nullable=False)

    jobs = relationship('Job', back_populates='cosplayer')

class CosplayerInput(Base):
    __tablename__ = 'cosplayer_inputs'

    id = Column(Integer, primary_key=True)
    background = Column(String(100))
    style = Column(String(100))
    character = Column(String(100))
    mood = Column(String(100))

    job_id = Column(Integer, ForeignKey('jobs.id'))
    job = relationship('Job', back_populates='cosplayer_input')

class ReferencePhoto(Base):
    __tablename__ = 'reference_photos'

    id = Column(Integer, primary_key=True)
    uploaded_at = Column(DateTime)

    job_id = Column(Integer, ForeignKey('jobs.id'))
    job = relationship('Job', back_populates='reference_photo')

class SelectedPhoto(Base):
    __tablename__ = 'selected_photos'

    id = Column(Integer, primary_key=True)
    selected_at = Column(DateTime)

    job_id = Column(Integer, ForeignKey('jobs.id'))
    job = relationship('Job', back_populates='selected_photos')

class GeneratedImage(Base):
    __tablename__ = 'generated_images'

    id = Column(Integer, primary_key=True)
    generated_at = Column(DateTime)

    job_id = Column(Integer, ForeignKey('jobs.id'))
    job = relationship('Job', back_populates='generated_images')

class FinalImage(Base):
    __tablename__ = 'final_images'

    id = Column(Integer, primary_key=True)
    is_printed = Column(Boolean, default=False)
    finalized_at = Column(DateTime)

    job_id = Column(Integer, ForeignKey('jobs.id'))
    job = relationship('Job', back_populates='final_image')

class Job(Base):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True)
    status = Column(String(50))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    cosplayer_id = Column(Integer, ForeignKey('cosplayers.id'))
    cosplayer = relationship('Cosplayer', back_populates='jobs')

    cosplayer_input = relationship('CosplayerInput', uselist=False, back_populates='job')
    reference_photo = relationship('ReferencePhoto', uselist=False, back_populates='job')
    selected_photos = relationship('SelectedPhoto', back_populates='job')
    generated_images = relationship('GeneratedImage', back_populates='job')
    final_image = relationship('FinalImage', uselist=False, back_populates='job')