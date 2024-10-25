# tests/level_3_tests.py

import unittest
from task_manager_impl import TaskManagerImpl

class Level3Tests(unittest.TestCase):
    
    @classmethod
    def setUp(cls):
        cls.task_manager = TaskManagerImpl()

    def test_complete_task(self):
        self.task_manager.add_task("Task 1")
        self.assertTrue(self.task_manager.complete_task("Task 1"))
        self.assertFalse(self.task_manager.complete_task("Task 2"))

    def test_filter_completed_tasks(self):
        self.task_manager.add_task("Task 1")
        self.task_manager.add_task("Task 2")
        self.task_manager.complete_task("Task 1")
        self.assertEqual(self.task_manager.filter_completed_tasks(), ["Task 1"])

if __name__ == '__main__':
    unittest.main()
