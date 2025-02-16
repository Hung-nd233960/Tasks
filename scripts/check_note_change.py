# pylint: disable = C0114
from typing import Optional
from task_parser import parse_task_line
from retrieve_task_hash import get_stored_task_hash
from scripts.func.model import TaskDetails, generate_task_hash


def check_note_file_change(file_path: str) -> Optional[TaskDetails]:
    """
    Check if a note has been changed in a file by comparing the SHA-1 hash
    of the note with the hash stored in the database.
    Parameters:
        file_path (str): The path to the file containing the note.
    Returns:
        Optional[TaskDetails]: The task details if the note has been changed,
        otherwise None.
    """
    # Get the SHA-1 hash of the note
    with open(file_path, "r", encoding="utf-8") as file:
        task_line = file.readline().strip()
        task = parse_task_line(task_line)
        task_hash = generate_task_hash(task) if task else None
    # Compare the hash with the stored hash
    stored_hash = get_stored_task_hash(task) if task else None
    if task_hash != stored_hash:
        return task
    return None
