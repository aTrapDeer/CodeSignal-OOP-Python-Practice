# tests/level_2_tests.py

import unittest
from task_manager_impl import TaskManagerImpl

class Level2Tests(unittest.TestCase):
    
    @classmethod
    def setUp(cls):
        cls.task_manager = TaskManagerImpl()

    def test_add_task_with_priority(self):
        self.task_manager.add_task("Task 1", 1)
        self.task_manager.add_task("Task 2", 3)
        self.assertEqual(self.task_manager.list_tasks(), ["Task 1", "Task 2"])

    def test_highest_priority_task(self):
        self.task_manager.add_task("Task 1", 1)
        self.task_manager.add_task("Task 2", 3)
        self.assertEqual(self.task_manager.get_highest_priority_task(), "Task 2")

if __name__ == '__main__':
    unittest.main()
