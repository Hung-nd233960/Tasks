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


def update_task_to_db(task: TaskDetails, db_path: str = "db/tasks.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Prepare dynamic SET clause based on non-None fields
    set_clauses = []
    values = []

    if task.get("content") is not None:
        set_clauses.append("content = ?")
        values.append(task["content"])

    if task.get("status") is not None:
        set_clauses.append("status = ?")
        values.append(task["status"])

    if task.get("scheduled_date") is not None:
        set_clauses.append("scheduled_date = ?")
        values.append(convert_date(task["scheduled_date"]))

    if task.get("start_date") is not None:
        set_clauses.append("start_date = ?")
        values.append(convert_date(task["start_date"]))

    if task.get("due_date") is not None:
        set_clauses.append("due_date = ?")
        values.append(convert_date(task["due_date"]))

    if task.get("priority") is not None:
        set_clauses.append("priority = ?")
        values.append(str(task["priority"]))

    new_hash = generate_task_hash(task)
    set_clauses.append("hash = ?")
    values.append(new_hash)

    # Always update modified_date
    set_clauses.append("modified_date = datetime('now')")

    # Construct final SQL query
    sql = f"""
        UPDATE tasks
        SET {', '.join(set_clauses)}
        WHERE id = ?
    """

    values.append(str(task["id"]))

    # Execute the query
    cursor.execute(sql, values)
    conn.commit()
    conn.close()
