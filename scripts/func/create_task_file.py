"""
Creates and writes to a Markdown file based on the details of a specified task.
The filename is constructed using a date (either the task's scheduled date
or the current date if none is provided), the task ID, and the task content,
formatted as: YYYY-id-content.md
Args:
    task (TaskDetails): An object containing information about the task,
        including 'id', 'content', and optionally 'scheduled_date'.
Returns:
    None: This function creates a file and prints a success message,
    but does not return any value.
"""

# pylint: disable=missing-function-docstring
from datetime import datetime
from func.model import TaskDetails
from func.task_line_creator import create_task_line


def create_task_file(task: TaskDetails, directory: str = "tasks/"):
    date_str = (
        task["scheduled_date"].strftime("%Y")
        if task["scheduled_date"]
        else datetime.now().strftime("%Y")
    )
    task_id = task["id"]
    content = task["content"]
    filename = f"{directory}{date_str}-{task_id}-{content}.md"

    # Create an empty file
    with open(filename, "w", encoding="utf-8") as file:
        file.write(create_task_line(task))

    print(f"File '{filename}' created successfully!")


# Example usage
if __name__ == "__main__":
    TASK = TaskDetails(
        id=1,
        content="Complete task creator function",
        status="undone",
        scheduled_date=datetime.strptime("2022-01-01", "%Y-%m-%d"),
        start_date=None,
        due_date=None,
        priority=None,
    )
    create_task_file(TASK)
