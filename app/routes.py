from flask import Blueprint, request, jsonify
from models import Job
from utils.job_queue import JobQueue
from app import session, job_queue

routes = Blueprint('routes', __name__)

@routes.route('/jobs', methods=['POST'])
def create_job():
    data = request.get_json()
    cosplayer_id = data['cosplayer_id']
    status = data['status']
    new_job = Job(cosplayer_id=cosplayer_id, status=status)
    session.add(new_job)
    session.commit()
    job_queue.enqueue(new_job)
    return jsonify({'message': 'Job created successfully'}), 201

@routes.route('/jobs', methods=['GET'])
def get_jobs():
    jobs = session.query(Job).all()
    job_data = []
    for job in jobs:
        job_data.append({
            'id': job.id,
            'cosplayer_id': job.cosplayer_id,
            'status': job.status
        })
    return jsonify(job_data), 200