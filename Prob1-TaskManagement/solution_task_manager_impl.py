## COPY ME over to task_manager_impl.py - this is the solution for you to reference or copy over to run.

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
        self.tasks = []
        pass

    def add_task(self, task: str, priority: int = 0, completed: bool = False) -> int:
        print("Adding task...")
        self.tasks.append({"task": task, "priority": priority, "completed": completed})
        print(f"Task {task} added with priority {priority}")
        print("")
        return len(self.tasks)

    def delete_task(self, task: str) -> bool:
        # need to check if the task exists
        print("Deleting task...")
        for t in self.tasks:
            # if the task exists, remove it from the list
            if t['task'] == task:
                self.tasks.remove(t)
                print(f"Task {task} deleted")
                print("")
                return True
        print("")
        return False


    def list_tasks(self) -> list:
        print("Listing tasks...")
        print(task['task'] for task in self.tasks)
        print(f"Total tasks: {len(self.tasks)}")
        print(self.tasks)
        print("")
        return [task['task'] for task in self.tasks]


    def get_highest_priority_task(self) -> str | None:
        print("Getting highest priority task...")
        if len(self.tasks) == 0:
            print("No tasks found")
            return None
        else:
            # Sort the tasks by priority
            sorting_tasks = sorted(self.tasks, key=lambda x: x['priority'], reverse=True)
            print(sorting_tasks)
            print(f"Highest priority task: {sorting_tasks[0]['task']}")
            print("")
            return sorting_tasks[0]['task']

    def complete_task(self, task: str) -> bool:
        # Completing a task
        print("Completing task...")
        # taking in a task, and checking if it exists and if the user wants to complete it
        for t in self.tasks:
            if t['task'] == task:
                t['completed'] = True
                print(f"Task {task} completed")
                print("")
                return True
            else:
                print(f"Task {task} not found")
                print("")
                return False
        return False
        

    def filter_completed_tasks(self) -> list:
        print("Filtering completed tasks...")
        completed_tasks = [task for task in self.tasks if task['completed']]
        print(completed_tasks)
        print(f"Total completed tasks: {len(completed_tasks)}")
        print("")
        return [task['task'] for task in completed_tasks]
