# Exercise 4: Todo List

## Overview
Build a simple todo list manager that can add, complete, and list tasks.

## Requirements

Create a `TodoList` class that manages a collection of tasks:

1. **Add tasks**: Add a new task with a description
2. **List all tasks**: Return all tasks with their status
3. **Complete tasks**: Mark a task as complete by its ID
4. **List pending tasks**: Return only incomplete tasks
5. **Remove tasks**: Delete a task by its ID

## Specifications

### Task Structure
Each task should have:
- `id`: Unique identifier (integer, auto-incremented starting from 1)
- `description`: String description of the task
- `completed`: Boolean status (default: False)

### Methods

- `add_task(description)`: Add a new task, return the task ID
- `get_all_tasks()`: Return a list of all tasks as dictionaries
- `complete_task(task_id)`: Mark a task as complete
- `get_pending_tasks()`: Return list of incomplete tasks
- `remove_task(task_id)`: Delete a task

### Error Handling
- Empty description should raise `ValueError`
- Invalid task ID should raise `ValueError`
- Completing/removing non-existent task should raise `ValueError`

## Example Usage

```python
todo = TodoList()

# Add tasks
id1 = todo.add_task("Buy groceries")      # Returns 1
id2 = todo.add_task("Walk the dog")       # Returns 2
id3 = todo.add_task("Finish homework")    # Returns 3

# Get all tasks
todo.get_all_tasks()
# Returns:
# [
#   {"id": 1, "description": "Buy groceries", "completed": False},
#   {"id": 2, "description": "Walk the dog", "completed": False},
#   {"id": 3, "description": "Finish homework", "completed": False}
# ]

# Complete a task
todo.complete_task(1)

# Get pending tasks
todo.get_pending_tasks()
# Returns:
# [
#   {"id": 2, "description": "Walk the dog", "completed": False},
#   {"id": 3, "description": "Finish homework", "completed": False}
# ]

# Remove a task
todo.remove_task(2)

# Error cases
todo.add_task("")           # Raises ValueError
todo.complete_task(999)     # Raises ValueError
```

## Tips

- Use a list or dictionary to store tasks internally
- Keep track of the next available ID
- Think about what happens when tasks are removed (ID gaps are OK)
- Make copies of tasks when returning them to avoid external modification

## Time Estimate
10-15 minutes
