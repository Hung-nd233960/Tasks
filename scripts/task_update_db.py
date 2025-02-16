"""
Update an existing task record in the SQLite database.
This function connects to the SQLite database specified by the `db_path`,
and updates the task record corresponding to the `id` provided in the `task`
dictionary. It updates the content, status, scheduled date, start date, due date,
priority, and automatically sets the modified_date to the current datetime.
Parameters:
    task (TaskDetails): A dictionary-like object containing the task data with
                        the following keys:
                        - "id": The unique identifier of the task.
                        - "content": The textual content of the task.
                        - "status": The current status of the task.
                        - "scheduled_date": The scheduled date of the task (can be None).
                        - "start_date": The start date of the task (can be None).
                        - "due_date": The due date of the task (can be None).
                        - "priority": The priority level of the task.
    db_path (str, optional): The file path to the SQLite database. Defaults to "db/tasks.db".
Returns:
    None
"""

# pylint: disable=C0116
# mypy: ignore-errors
import sqlite3
from scripts.func.model import TaskDetails, convert_date, generate_task_hash


def update_task_to_db(task: TaskDetails, db_path: str = "db/tasks.db") -> bool:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Prepare fields for update (including None values explicitly)
    set_clauses = [
        "content = ?",
        "status = ?",
        "scheduled_date = ?",
        "start_date = ?",
        "due_date = ?",
        "priority = ?",
        "hash = ?",
        "modified_date = datetime('now')",
    ]

    values = [
        task["content"],
        task["status"],
        convert_date(task["scheduled_date"]) if task["scheduled_date"] else None,
        convert_date(task["start_date"]) if task["start_date"] else None,
        convert_date(task["due_date"]) if task["due_date"] else None,
        str(task["priority"]) if task["priority"] is not None else None,
        generate_task_hash(task),  # Always update hash
    ]

    # Append task ID for WHERE clause
    values.append(task["id"])

    # Construct and execute query
    sql = f"""
        UPDATE tasks
        SET {', '.join(set_clauses)}
        WHERE id = ?
    """

    cursor.execute(sql, values)
    success = cursor.rowcount > 0  # Check if any row was updated
    conn.commit()
    conn.close()

    return success
