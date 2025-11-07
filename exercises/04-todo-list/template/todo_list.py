"""
Todo List Module

Implement a simple todo list manager.
"""


class TodoList:
    """A simple todo list manager for tracking tasks."""

    def __init__(self):
        """Initialize an empty todo list."""
        pass

    def add_task(self, description):
        """Add a new task to the list.

        Args:
            description: String description of the task.

        Returns:
            Integer ID of the newly created task.

        Raises:
            ValueError: If description is empty or whitespace only.
        """
        pass

    def get_all_tasks(self):
        """Get all tasks in the list.

        Returns:
            List of dictionaries with keys: id, description, completed.
        """
        pass

    def complete_task(self, task_id):
        """Mark a task as completed.

        Args:
            task_id: Integer ID of the task to complete.

        Raises:
            ValueError: If task_id doesn't exist.
        """
        pass

    def get_pending_tasks(self):
        """Get all incomplete tasks.

        Returns:
            List of dictionaries for tasks where completed is False.
        """
        pass

    def remove_task(self, task_id):
        """Remove a task from the list.

        Args:
            task_id: Integer ID of the task to remove.

        Raises:
            ValueError: If task_id doesn't exist.
        """
        pass
