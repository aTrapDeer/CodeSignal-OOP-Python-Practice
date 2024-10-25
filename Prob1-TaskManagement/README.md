## Implement a task management system that tracks tasks and their priorities.

Project Overview:
- Level 1: Basic functionality for adding, deleting, and listing tasks.
- Level 2: Add support for prioritizing tasks and retrieving the highest priority task.
- Level 3: Add support for completing tasks and filtering tasks based on their completion status.
### Code Skeleton:
Let's start by creating the structure for the code. TaskManager will implement all the features progressively over 3 levels. You’ll start by implementing basic functionality, then add features for task prioritization and task completion.

_________

### Example Project Document (Additional Information):

#### Project Overview: **Task Management System**

##### Purpose:
To implement a Task Management System where users can add, delete, prioritize, complete, and filter tasks. The system is built using object-oriented programming principles, providing a clean and modular structure.

##### Levels of Functionality:

- **Level 1**: Basic task operations such as adding, deleting, and listing tasks.
- **Level 2**: Prioritization of tasks and retrieving the task with the highest priority. Descending order of priority.
- **Level 3**: Task completion and filtering completed tasks.

##### Core Components:

1. **TaskManager Class (Base Class)**:
   - Acts as an abstract class defining the core functionalities (`add_task`, `delete_task`, `list_tasks`, `get_highest_priority_task`, `complete_task`, `filter_completed_tasks`).
   
2. **TaskManagerImpl Class (Implementation Class)**:
   - This class implements the functionalities defined in `TaskManager`.
   - The class holds a list of tasks where each task is a dictionary with fields like task name, priority, and completion status.

##### Testing:
- Unit tests are provided for each level of functionality.
- The tests progressively unlock as each level is completed and the core functionality is implemented.

##### File Structure:

```
project/
├── task_manager.py                 # Abstract class and implementation
├── tests/
│   ├── level_1_tests.py            # Tests for basic task operations
│   ├── level_2_tests.py            # Tests for task prioritization
│   ├── level_3_tests.py            # Tests for task completion
```

##### Example Task Flow:

- **Level 1**:
  - Add task: `"Submit project report"`
  - Delete task: `"Buy groceries"`
  - List tasks: `["Submit project report", "Buy groceries"]`
  
- **Level 2**:
  - Add task with priority: `"Fix critical bug", priority 3`
  - Highest priority task: `"Fix critical bug"`

- **Level 3**:
  - Complete task: `"Submit project report"`
  - Filter completed tasks: `["Submit project report"]`

