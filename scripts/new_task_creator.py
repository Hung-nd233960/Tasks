from typing import Optional
from func.model import TaskDetails
from func.create_task_file import create_task_file
from func.task_import_db import insert_new_task_to_db


def new_task_creator(task: TaskDetails) -> Optional[int]:
    """
    Create a new task file and store the task details in the database.
    Parameters:
        task (TaskDetails): An object containing information about the task.
    Returns:
        None: This function creates a file and stores the task details in the database,
        but does not return any value.
    """
    # Create a Markdown file for the task

    # Store the task details in the database
    new_task_id = insert_new_task_to_db(task)
    task["id"] = new_task_id
    create_task_file(task)
    return new_task_id


if __name__ == "__main__":
    from datetime import datetime

    TASK = TaskDetails(
        id=1,
        content="Complete task creator function",
        status="undone",
        scheduled_date=datetime.strptime("2022-01-01", "%Y-%m-%d"),
        start_date=None,
        due_date=None,
        priority=None,
    )
    new_task_creator(TASK)
