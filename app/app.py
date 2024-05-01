from flask import Flask, request, jsonify, render_template, Blueprint
from .models import Job, Session, engine
import os

app = Blueprint('app', __name__)

def create_job_directories(job_id):
    base_path = f"jobs/{job_id}"
    directories = [
        base_path,
        f"{base_path}/raw",
        f"{base_path}/controlnet_assets",
        f"{base_path}/ipadapter",
        f"{base_path}/masks",
        f"{base_path}/generated_images"
    ]
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

@app.route('/')
def home():
    return render_template('check_in.html')

@app.route('/jobs', methods=['POST'])
def create_job():
    session = Session()
    nickname = request.form['nickname']
    new_job = Job(nickname=nickname)
    session.add(new_job)
    session.commit()

    # Erstelle die Ordnerstruktur für den neuen Job
    create_job_directories(new_job.id)

    return jsonify({"job_id": new_job.id, "job_url": new_job.job_url}), 201

@app.route('/jobs', methods=['GET'])
def get_jobs():
    session = Session()
    jobs = session.query(Job).all()
    jobs_data = [{
        "id": job.id,
        "nickname": job.nickname,
        "status": job.status,
        "job_url": job.job_url
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
            session.commit()
            return jsonify({"message": "Job status updated to " + new_status}), 200
        else:
            return jsonify({"error": "Invalid status provided"}), 400
    return jsonify({"error": "Job not found"}), 404

@app.route('/jobs/<job_id>', methods=['GET'])
def get_job(job_id):
    session = Session()
    job = session.query(Job).filter_by(id=job_id).first()
    if job:
        return jsonify({
            "nickname": job.nickname,
            "status": job.status,
            "job_url": job.job_url
        })
    return jsonify({"error": "Job not found"}), 404
