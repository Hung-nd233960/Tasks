# pylint: disable=missing-module-docstring
import sqlite3
from typing import Optional
from model import TaskDetails


def get_stored_task_hash(task: TaskDetails, db: str = "db/tasks.db") -> Optional[str]:
    """
    Retrieve the stored SHA-1 hash of a task from the database using its ID.

    Parameters:
        task (TaskDetails): The task dictionary containing task details, including the ID.
        db (str): Path to the SQLite database. Defaults to 'db/tasks.db'.

    Returns:
        Optional[str]: The stored SHA-1 hash if found, otherwise None.
    """
    task_id = task.get("id")
    if task_id is None:
        raise ValueError("Task ID is missing. Cannot retrieve hash without ID.")

    # Connect to the database and retrieve the stored hash
    try:
        conn = sqlite3.connect(db)
        cursor = conn.cursor()

        # Assuming your tasks table has columns: id, hash
        cursor.execute("SELECT hash FROM tasks WHERE id = ?", (task_id,))
        result = cursor.fetchone()

        conn.close()

        if result:
            return result[0]  # Return the hash from the query
        print(f"No hash found for task ID {task_id}.")
        return None

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None
