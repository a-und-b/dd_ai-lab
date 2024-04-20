from models import Job
from app import session, job_queue

class JobService:
    @staticmethod
    def process_jobs():
        while not job_queue.is_empty():
            job = job_queue.dequeue()
            # Verarbeite den Job basierend auf dem Status
            if job.status == 'new':
                # Führe Aktionen für neue Jobs aus
                job.status = 'processing'
            elif job.status == 'processing':
                # Führe Aktionen für Jobs in Bearbeitung aus
                job.status = 'completed'
            elif job.status == 'completed':
                # Führe Aktionen für abgeschlossene Jobs aus
                pass
            # Aktualisiere den Job-Status in der Datenbank
            session.commit()