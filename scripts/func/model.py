# pylint: disable=missing-module-docstring, missing-class-docstring, missing-function-docstring
from datetime import datetime
from typing import Optional, TypedDict
from hashlib import sha1
import sqlite3


class TaskDetails(TypedDict):
    status: str
    content: str
    scheduled_date: Optional[datetime]
    start_date: Optional[datetime]
    due_date: Optional[datetime]
    priority: Optional[int]
    id: Optional[int]


def convert_date(date_obj: Optional[datetime]) -> Optional[str]:
    return date_obj.strftime("%Y-%m-%d") if isinstance(date_obj, datetime) else date_obj


def generate_task_hash(task: TaskDetails) -> str:
    """
    Generate a SHA-1 hash for the task based on its content and key fields.
    """
    # Concatenate the task fields into a single string for hashing
    task_string = f"{task['content']}|{task['status']}|{task.get('scheduled_date', '')}|{task.get('start_date', '')}|{task.get('due_date', '')}|{task['priority']}"

    # Encode and generate SHA-1 hash
    task_hash = sha1(task_string.encode("utf-8")).hexdigest()

    return task_hash


def get_stored_task(task_id: int, db_path: str = "db/tasks.db") -> TaskDetails:
    """
    Retrieve a task from the database using its ID.

    Parameters:
        task_id (int): The ID of the task to retrieve.
        db_path (str): The path to the database file.

    Returns:
        TaskDetails: The task details stored in the database.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT status, content, scheduled_date, start_date, due_date, priority, id FROM tasks WHERE id = ?",
        (task_id,),
    )
    row = cursor.fetchone()
    conn.close()

    if row:
        return TaskDetails(
            status=row[0],
            content=row[1],
            scheduled_date=row[2],
            start_date=row[3],
            due_date=row[4],
            priority=row[5],
            id=row[6],
        )

    raise ValueError(f"Task with ID {task_id} not found in database.")
