# tests/level_1_tests.py

import unittest
from task_manager_impl import TaskManagerImpl

class Level1Tests(unittest.TestCase):
    
    @classmethod
    def setUp(cls):
        cls.task_manager = TaskManagerImpl()

    def test_add_task(self):
        self.assertEqual(self.task_manager.add_task("Task 1"), 1)
        self.assertEqual(self.task_manager.add_task("Task 2"), 2)

    def test_delete_task(self):
        self.task_manager.add_task("Task 1")
        self.task_manager.add_task("Task 2")
        self.assertTrue(self.task_manager.delete_task("Task 1"))
        self.assertFalse(self.task_manager.delete_task("Task 3"))

    def test_list_tasks(self):
        self.task_manager.add_task("Task 1")
        self.task_manager.add_task("Task 2")
        self.assertEqual(self.task_manager.list_tasks(), ["Task 1", "Task 2"])

if __name__ == '__main__':
    unittest.main()
