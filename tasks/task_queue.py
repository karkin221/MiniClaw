
class TaskQueue:

    def __init__(self):

        self.queue = []

    def add_task(self, task):

        self.queue.append(task)

    def process_tasks(self):

        while self.queue:

            task = self.queue.pop(0)

            print(f"[Background Task] {task}")
