"""
Delete a task from the database.
This function deletes a task from the database based on the provided
task_id or a combination of content and scheduled_date. If neither
task_id nor both content and scheduled_date are provided, a ValueError
is raised.
Args:
    task_id (int, optional): The ID of the task to delete. Defaults to None.
    content (str, optional): The content of the task to delete. Defaults to None.
    scheduled_date (str, optional): The scheduled date of the task to delete. Defaults to None.
    db_path (str, optional): The path to the database file. Defaults to "db/tasks.db".
Raises:
    ValueError: If neither task_id nor both content and scheduled_date are provided.
Example:
    delete_task_from_db(task_id=1)
    delete_task_from_db(content="Task content", scheduled_date="2023-10-01")
"""

# pylint: disable=C0116
import sqlite3
from typing import Optional
from scripts.func.model import TaskDetails


def delete_task_from_db(
    task_obj: Optional[TaskDetails] = None,
    task_id: Optional[int] = None,
    content: Optional[str] = None,
    scheduled_date: Optional[str] = None,
    db_path="db/tasks.db",
):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    if task_obj:
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_obj["id"],))
    if task_id:
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    elif content and scheduled_date:
        cursor.execute(
            "DELETE FROM tasks WHERE content = ? AND scheduled_date = ?",
            (content, scheduled_date),
        )
    else:
        raise ValueError(
            "Either task_id or both content and scheduled_date must be provided."
        )

    if cursor.rowcount == 0:
        print(
            "No task was deleted. Please check the provided task_id or content and scheduled_date."
        )

    conn.commit()
    conn.close()


if __name__ == "__main__":
    delete_task_from_db(task_id=1)
    # delete_task_from_db(content="Task content", scheduled_date="2023-10-01")
    print("Task deleted successfully.")
