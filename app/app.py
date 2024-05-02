from flask import Flask, request, jsonify, render_template, Blueprint
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from .utils import create_job_directories, generate_qr_code
import hashlib
import os

Base = declarative_base()

def generate_job_id(nickname):
    timestamp = int(datetime.utcnow().timestamp())
    timestamp_str = str(timestamp)[-3:]
    nickname_hash = hashlib.sha256(nickname.encode()).hexdigest()[:3]
    return f"{timestamp_str}{nickname_hash}"

class Job(Base):
    __tablename__ = 'jobs'
    id = Column(String, primary_key=True, default=lambda context: generate_job_id(context.get_current_parameters()['nickname']))
    job_number = Column(Integer, unique=True)
    nickname = Column(String)
    character = Column(String)
    fandom = Column(String)
    background = Column(Text)
    mood = Column(String)
    style = Column(String)
    status = Column(String, default='new')
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    job_url = Column(String, default=lambda context: f"https://andersundbesser.de/lfg/{context.get_current_parameters()['id']}")

engine = create_engine('sqlite:///cosplay.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

app = Blueprint('app', __name__)

@app.route('/')
def home():
    return render_template('check_in.html')

@app.route('/jobs', methods=['POST'])
def create_job():
    session = Session()
    last_job = session.query(Job).order_by(Job.job_number.desc()).first()
    next_job_number = (last_job.job_number + 1) if last_job else 1

    new_job = Job(
        nickname=request.form['nickname'],
        character=request.form['character'],
        fandom=request.form['fandom'],
        background=request.form['background'],
        mood=request.form['mood'],
        style=request.form['style'],
        job_number=next_job_number
    )
    session.add(new_job)
    session.commit()

    create_job_directories(new_job.id)
    generate_qr_code(new_job.id, new_job.job_url)

    return jsonify({"job_id": new_job.id, "job_number": new_job.job_number, "job_url": new_job.job_url}), 201


@app.route('/jobs', methods=['GET'])
def get_jobs():
    session = Session()
    jobs = session.query(Job).all()
    jobs_data = [{
        "id": job.id,
        "job_number": job.job_number,
        "nickname": job.nickname,
        "character": job.character,
        "fandom": job.fandom,
        "background": job.background,
        "mood": job.mood,
        "style": job.style,
        "status": job.status,
        "created_at": job.created_at.isoformat(),  # Konvertiere in ISO-Format für JSON
        "updated_at": job.updated_at.isoformat() if job.updated_at else None,
        "job_url": job.job_url,
        "qr_code_url": f"/static/jobs/{job.id}/qr_code.png"
    } for job in jobs]
    return jsonify(jobs_data)



@app.route('/jobs/<job_id>', methods=['PUT'])
def update_job_status(job_id):
    session = Session()
    job = session.query(Job).filter_by(id=job_id).first()
    if job:
        new_status = request.json.get('status')
        if new_status in ['new', 'shooting', 'assets-ready', 'processing', 'output-ready', 'finished']:
            job.status = new_status
            job.updated_at = datetime.utcnow()  # Aktualisiere updated_at
            session.commit()
            return jsonify({"message": "Job status updated to " + new_status}), 200
        else:
            return jsonify({"error": "Invalid status provided"}), 400
    return jsonify({"error": "Job not found"}), 404


@app.route('/jobs/<job_id>/images')
def get_job_images(job_id):
    job_dir = f"app/static/jobs/{job_id}"
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    images = []

    for root, dirs, files in os.walk(job_dir):
        for file in files:
            if os.path.splitext(file)[1].lower() in image_extensions:
                images.append({
                    'filename': file,
                    'url': f"/static/jobs/{job_id}/{file}"
                })

    return jsonify(images)

@app.route('/gallery.html')
def gallery():
    return render_template('gallery.html')

def create_app():
    app = Flask(__name__)
    app.register_blueprint(app)
    return app
