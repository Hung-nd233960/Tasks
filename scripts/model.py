# pylint: disable=missing-module-docstring, missing-class-docstring, missing-function-docstring
from datetime import datetime
from typing import Optional, TypedDict
from hashlib import sha1


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
