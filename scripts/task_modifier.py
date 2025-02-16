import os
from scripts.func.model import TaskDetails, get_stored_task
from task_update_db import update_task_to_db
from scripts.func.task_line_creator import create_task_line


def edit_task(
    task: TaskDetails, db_path: str = "db/tasks.db", task_dir: str = "tasks/"
):
    """
    Edit an existing task by comparing changes to the database,
    updating the database, retrieving the updated task, and overriding
    the task line in the corresponding Markdown file.

    Parameters:
        task (TaskDetails): The updated task details.
        db_path (str): The database file path.
        task_dir (str): The directory where task files are stored.
    """
    # Retrieve existing task from the database
    existing_task = get_stored_task(task["id"], db_path)
    if not existing_task:
        print("Task not found in the database.")
        return

    # Compare changes
    valid_keys = ["id", "status", "content", "scheduled_date", "start_date", "due_date"]
    changes = {}
    for key in valid_keys:
        if task[key] != existing_task.get(key):
            changes[key] = task[key]
    if not changes:
        print("No changes detected.")
        return

    # Update database with new values
    update_task_to_db(task, db_path)

    # Retrieve the updated task
    updated_task = get_stored_task(task["id"], db_path)
    if not updated_task:
        print("Error retrieving updated task from database.")
        return

    # Generate new task line
    new_task_line = create_task_line(updated_task)

    # Find corresponding Markdown file
    task_id = task["id"]
    for filename in os.listdir(task_dir):
        if f"-{task_id}-" in filename:
            file_path = os.path.join(task_dir, filename)
            break
    else:
        print("No corresponding Markdown file found.")
        return

    # Replace first line with the new task line
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    lines[0] = new_task_line + "\n"

    with open(file_path, "w", encoding="utf-8") as file:
        file.writelines(lines)

    print(f"Task {task_id} updated successfully.")
