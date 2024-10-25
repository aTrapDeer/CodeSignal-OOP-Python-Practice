# task_manager.py
# Solve in here 
from abc import ABC, abstractmethod

class TaskManager(ABC):
    """
    The base class for Task Manager
    """

    @abstractmethod
    def add_task(self, task: str, priority: int = 0) -> int:
        """
        Add a task to the task manager.
        Should return the number of tasks after addition.
        """
        pass

    @abstractmethod
    def delete_task(self, task: str) -> bool:
        """
        Delete a task from the task manager.
        Should return True if the task is successfully deleted, else False.
        """
        pass

    @abstractmethod
    def list_tasks(self) -> list:
        """
        List all the tasks in the task manager.
        """
        pass

    @abstractmethod
    def get_highest_priority_task(self) -> str | None:
        """
        Return the task with the highest priority.
        If no tasks are present, return None.
        """
        pass

    @abstractmethod
    def complete_task(self, task: str) -> bool:
        """
        Mark a task as completed.
        Should return True if the task is successfully marked as complete, else False.
        """
        pass

    @abstractmethod
    def filter_completed_tasks(self) -> list:
        """
        Return a list of tasks that have been marked as completed.
        """
        pass


class TaskManagerImpl(TaskManager):
    def __init__(self):
        pass

    def add_task(self, task: str) -> int:
        pass

    def delete_task(self, task: str) -> bool:
        pass


    def list_tasks(self) -> list:
        pass


    def get_highest_priority_task(self) -> str | None:
        pass

    def complete_task(self, task: str) -> bool:
        pass
        

    def filter_completed_tasks(self) -> list:
        pass
