# pylint: disable=missing-module-docstring
# mypy: ignore-errors

from datetime import datetime
from func.model import TaskDetails


def create_task_line(task: TaskDetails) -> str:
    """
    Generate a Markdown-formatted task line from a TaskDetails object.

    Parameters:
        task (TaskDetails): An object containing task details.

    Returns:
        str: A Markdown-formatted string representing the task.
    """
    # Determine the task status marker
    status_marker = "x" if task.get("status") == "done" else " "

    # Start with the basic task format
    task_line = f"- [{status_marker}] #task {task.get('content', '')}"

    # Append optional fields if they exist
    if task.get("scheduled_date"):
        task_line += (
            f" [scheduled:: {task['scheduled_date'].strftime('%Y-%m-%d')}]"
            if task.get("scheduled_date") not in ["", None]
            else ""
        )

    if task.get("start_date"):
        task_line += (
            f" [start:: {task['start_date'].strftime('%Y-%m-%d')}]"
            if task.get("start_date") not in ["", None]
            else ""
        )

    if task.get("due_date"):
        task_line += (
            f" [due:: {task['due_date'].strftime('%Y-%m-%d')}]"
            if task.get("due_date") not in ["", None]
            else ""
        )

    if task.get("priority") is not None:
        task_line += (
            f" [priority:: {task['priority']}]"
            if task.get("priority") not in ["", None]
            else ""
        )

    if task.get("id") is not None:
        task_line += f" [id:: {task['id']}]" if task.get("id") not in ["", None] else ""

    return task_line


# Example usage
if __name__ == "__main__":
    TASK_DETAILS = {
        "status": "undone",
        "content": "Finish the report",
        "scheduled_date": None,
        "start_date": None,
        "due_date": datetime(2025, 2, 28),
        "priority": 2,
        "id": 123,
    }

    TASK_LINE = create_task_line(TASK_DETAILS)
    print(TASK_LINE)
