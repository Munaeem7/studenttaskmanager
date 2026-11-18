import os
import sys
import unittest
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from task_manager import TaskManager
class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()
    def test_add_task(self):
        task = self.manager.add_task("Study for exam")
        self.assertEqual(task["title"], "Study for exam")
        self.assertEqual(len(self.manager.list_tasks()), 1)
    def test_complete_task(self):
        task = self.manager.add_task("Finish lab")
        self.manager.complete_task(task["id"])
        self.assertTrue(self.manager.list_tasks()[0]["completed"])
    def test_delete_task(self):
        task = self.manager.add_task("Old task")
        self.manager.delete_task(task["id"])
        self.assertEqual(self.manager.list_tasks(), [])
if __name__ == "__main__":
    unittest.main()
