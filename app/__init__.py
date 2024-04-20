from utils.database import create_database, create_session
from utils.job_queue import JobQueue

engine = create_database()
session = create_session(engine)
job_queue = JobQueue()

# Beispielcode zur Verwendung der JobQueue
def create_job(cosplayer_id, status):
    new_job = Job(cosplayer_id=cosplayer_id, status=status)
    session.add(new_job)
    session.commit()
    job_queue.enqueue(new_job)

def process_jobs():
    while not job_queue.is_empty():
        job = job_queue.dequeue()
        # Verarbeite den Job basierend auf dem Status
        if job.status == 'new':
            # Führe Aktionen für neue Jobs aus
            pass
        elif job.status == 'processing':
            # Führe Aktionen für Jobs in Bearbeitung aus
            pass
        elif job.status == 'completed':
            # Führe Aktionen für abgeschlossene Jobs aus
            pass
        # Aktualisiere den Job-Status in der Datenbank
        session.commit()