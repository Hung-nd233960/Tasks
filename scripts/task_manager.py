from typing import List
from git_file_change import get_repo_file_changes
from check_note_change import check_note_file_change
from task_parser import TaskDetails
from task_update_db import update_task_to_db


def find_changed_tasks() -> List[TaskDetails]:
    """
    Find all tasks that have been changed in the repository."""
    changed_files = get_repo_file_changes()["changed"]
    changed_tasks = []
    for file_path in changed_files:
        if file_path.startswith("tasks/"):
            changes = check_note_file_change(file_path)
            if changes:
                changed_tasks.append(changes)
    return changed_tasks


def update_changed_tasks():
    """
    Update all tasks that have been changed in the repository compare to last commit."""
    changed_tasks = find_changed_tasks()
    for task in changed_tasks:
        update_task_to_db(task)
    print(f"Updated {len(changed_tasks)} tasks.")
