import json
from pathlib import Path


class TaskManager:
    def __init__(self, storage_file=None):
        self.storage_file = Path(storage_file) if storage_file else None
        self.tasks = []
        self.next_id = 1
        self._load()

    def add_task(self, title):
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty.")
        title = title.strip()
        if len(title) > 100:
            raise ValueError("Task title must be 100 characters or less.")
        task = {"id": self.next_id, "title": title, "completed": False}
        self.tasks.append(task)
        self.next_id += 1
        self._save()
        return task

    def list_tasks(self):
        return self.tasks

    def complete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                if task["completed"]:
                    raise ValueError(f"Task {task_id} is already completed.")
                task["completed"] = True
                self._save()
                return task
        return None

    def delete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                self.tasks.remove(task)
                self._save()
                return True
        return False

    def _load(self):
        if self.storage_file and self.storage_file.exists():
            data = json.loads(self.storage_file.read_text())
            self.tasks = data["tasks"]
            self.next_id = data["next_id"]

    def _save(self):
        if self.storage_file:
            data = {"tasks": self.tasks, "next_id": self.next_id}
            self.storage_file.write_text(json.dumps(data, indent=2))