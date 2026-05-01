import json
import os
import uuid



class TaskManager:
    def __init__(self, file_path="data/tasks.json"):
        self.file_path = file_path

        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as f:
                json.dump([], f, ensure_ascii=False, indent=4)

    def load_tasks(self):
        with open(self.file_path, "r") as f:
            return json.load(f)

    def save_tasks(self, tasks):
        with open(self.file_path, "w") as f:
            json.dump(tasks, f, indent=4)

    def add_task(self, title, priority):
        tasks = self.load_tasks()

        task = {
            "id": str(uuid.uuid4()),
            "title": title,
            "priority": priority,
            "status": "Pending"
        }

        tasks.append(task)
        self.save_tasks(tasks)

    def get_tasks(self):
        tasks = self.load_tasks()

        priority_order = {"High": 3, "Medium": 2, "Low": 1}
        tasks.sort(key=lambda x: priority_order[x["priority"]], reverse=True)

        return tasks

    def mark_done(self, task_id):
        tasks = self.load_tasks()

        for task in tasks:
            if task["id"] == task_id:
                task["status"] = "Done"

        self.save_tasks(tasks)

    def delete_task(self, task_id):
        tasks = self.load_tasks()
        tasks = [t for t in tasks if t["id"] != task_id]
        self.save_tasks(tasks)