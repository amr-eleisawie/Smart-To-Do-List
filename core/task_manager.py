import json
import os
from datetime import datetime

class TaskManager:
    def __init__(self, file_path="data/tasks.json"):
        self.file_path = file_path
        self.tasks = self.load_tasks()

    def load_tasks(self):
        """Load tasks from JSON file"""
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as f:
                return json.load(f)
        return []

    def save_tasks(self):
        """Save tasks to JSON file"""
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        with open(self.file_path, 'w') as f:
            json.dump(self.tasks, f, indent=2)

    def add_task(self, title, priority="Medium"):
        """Add a new task"""
        task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "priority": priority,
            "status": "Pending",
            "created_at": datetime.now().isoformat()
        }
        self.tasks.append(task)
        self.save_tasks()
        return task

    def get_tasks(self):
        """Get all tasks"""
        return self.tasks

    def mark_done(self, task_id):
        """Mark a task as done"""
        for task in self.tasks:
            if task["id"] == task_id:
                task["status"] = "Done"
                self.save_tasks()
                return task
        return None

    def delete_task(self, task_id):
        """Delete a task"""
        self.tasks = [task for task in self.tasks if task["id"] != task_id]
        self.save_tasks()

    def get_task(self, task_id):
        """Get a specific task"""
        for task in self.tasks:
            if task["id"] == task_id:
                return task
        return None