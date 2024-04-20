from collections import deque

class JobQueue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, job):
        self.queue.append(job)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.popleft()

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)