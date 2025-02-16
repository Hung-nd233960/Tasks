"""
Insert a task record into the 'tasks' SQLite database.
Parameters
----------
task : dict
    A dictionary containing the task details. It should have the following keys:
        - id (int): Unique identifier of the task.
        - content (str): Description or content of the task.
        - status (str): The current status of the task (e.g., TODO, DONE).
        - scheduled_date (str): The scheduled date for the task in YYYY-MM-DD format.
        - start_date (str): The start date/time for the task in an accepted date/time format.
        - end_date (str): The end date/time for the task in an accepted date/time format.
        - priority (int): Numeric representation of priority (e.g., 1, 2, 3).
db_path : str, optional
    Path to the SQLite database file. Defaults to "db/task.db".
Returns
-------
int: The ID of the newly inserted task record.
"""

# pylint: disable=C0116
import sqlite3
from typing import Optional
from func.model import TaskDetails, convert_date, generate_task_hash


def insert_new_task_to_db(
    task: TaskDetails, db_path: str = "db/tasks.db"
) -> Optional[int]:
    """
    Insert a task into the SQLite database with SHA-1 hash for tracking changes.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Generate the hash for the task
    task_hash = generate_task_hash(task)

    # Insert the task into the database
    cursor.execute(
        """
        INSERT OR IGNORE INTO tasks (id, content, status, scheduled_date, start_date, due_date, priority, hash, created_date, modified_date)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, datetime('now'), datetime('now'))
        """,
        (
            task["id"],
            task["content"],
            task["status"],
            convert_date(task["scheduled_date"]) if task["scheduled_date"] else None,
            convert_date(task["start_date"]) if task["start_date"] else None,
            convert_date(task["due_date"]) if task["due_date"] else None,
            task["priority"],
            task_hash,  # Insert the hash here
        ),
    )
    new_task_id = cursor.lastrowid

    conn.commit()
    conn.close()

    return new_task_id


if __name__ == "__main__":
    from datetime import datetime

    TASK = TaskDetails(
        id=1,
        content="Complete task parser function",
        status="undone",
        scheduled_date=datetime.strptime("2022-01-01", "%Y-%m-%d"),
        start_date=datetime.strptime("2022-01-02", "%Y-%m-%d"),
        due_date=datetime.strptime("2022-01-03", "%Y-%m-%d"),
        priority=2,
    )
    task_id = insert_new_task_to_db(TASK)
    print(f"Task {task_id} inserted successfully.")
