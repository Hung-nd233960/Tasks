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
Returns:
    bool: True if the task was deleted successfully, False otherwise.
Example:
    delete_task_from_db(task_id=1)
    delete_task_from_db(content="Task content", scheduled_date="2023-10-01")
"""

import sqlite3
import os
from typing import Optional


def delete_task(
    task_id: Optional[int] = None,
    content: Optional[str] = None,
    scheduled_date: Optional[str] = None,
    db_path="db/tasks.db",
) -> bool:
    """
    Delete a task from the database and its corresponding file.

    Args:
        task_id (int, optional): The ID of the task to delete.
        content (str, optional): The content of the task to delete.
        scheduled_date (str, optional): The scheduled date of the task to delete.
        db_path (str, optional): The path to the database file.

    Returns:
        bool: True if the task was deleted successfully, False otherwise.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    if task_id:
        # Delete by ID
        cursor.execute(
            "SELECT content, scheduled_date FROM tasks WHERE id = ?", (task_id,)
        )
        task = cursor.fetchone()
        if task:
            file_path = f"tasks/{task[1][:4]}-{task_id}-{task[0]}.md"
            cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
            # delete_file(file_path)
        else:
            print("Task ID not found.")
            conn.close()
            return False

    elif content and scheduled_date:
        # Retrieve ID first, then delete
        cursor.execute(
            "SELECT id FROM tasks WHERE content = ? AND scheduled_date = ?",
            (content, scheduled_date),
        )
        task = cursor.fetchone()
        if task:
            task_id = task[0]
            file_path = f"tasks/{scheduled_date[:4]}-{task_id}-{content}.md"
            print(file_path)
            cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
            # delete_file(file_path)
        else:
            print("Task with given content and date not found.")
            conn.close()
            return False

    else:
        print("Provide either a task ID or both content and scheduled date.")
        conn.close()
        return False

    conn.commit()
    conn.close()
    print("Task deleted successfully.")
    return True


def delete_file(file_path: str) -> None:
    """
    Delete a file from the filesystem.

    Args:
        file_path (str): The path to the file to be deleted.
    """
    try:
        os.remove(file_path)
        print(f"File {file_path} deleted successfully.")
    except FileNotFoundError:
        print(f"File {file_path} not found.")


if __name__ == "__main__":
    delete_task(task_id=1)
    # delete_task_from_db(content="Task content", scheduled_date="2023-10-01")
    print("Task deleted successfully.")
