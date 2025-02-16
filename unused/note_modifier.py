import re
from check_note_change import check_note_file_change
from git_file_change import get_repo_file_changes
from task_update_db import update_task_to_db


def note_modifier(repo_path: str = ".", db_path: str = "db/tasks.db"):
    """
    Check if the repository contains any task file that have been changed.
    Then, check for the changes in the task data
    and update the database with the new task details.
    """
    # Get the list of changed files in the repository
    file_changes = get_repo_file_changes(repo_path)
    changed_files = file_changes["changed"]
    for file in changed_files:
        # Check if the file is a task file
        if re.match(r"^\d{4}-ID-.*\.md$", file):
            # Check if the note in the file has been changed
            task = check_note_file_change(file)
            if task:
                # Update the task in the database
                update_task_to_db(task, db_path)
        else:
            print(f"File '{file}' is not a task file. Skipping...")

