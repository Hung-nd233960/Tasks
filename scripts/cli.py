"""
This module defines a command-line interface (CLI) for managing tasks with three primary commands:
- init: Initializes the system.
- add: Adds a new task.
- delete: Deletes a task by ID or by (scheduled-date AND content).

Command-line Usage:
-------------------
Run 'python cli.py' followed by the desired command and corresponding arguments.
For example:
    python cli.py add "Complete report" --schedule-date 2023-10-05
    python cli.py delete --id 5
    python cli.py delete --schedule-date 2023-10-05 --content "Complete report"
"""

import argparse
import datetime
from func.model import TaskDetails
from new_task_creator import new_task_creator
from task_delete import delete_task
from init_system import init
from reset_system import reset


def validate_date(date_str):
    """Validate and parse a date string in YYYY-MM-DD format."""
    try:
        return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError as exc:
        raise argparse.ArgumentTypeError(
            "Invalid date format. Use YYYY-MM-DD."
        ) from exc


def add_task(_args):
    """Handles the 'add' command by creating and storing a new task."""
    task = TaskDetails(
        status="undone",  # Default status is undone
        content=_args.content,
        scheduled_date=_args.schedule_date,
        start_date=_args.start_date,
        due_date=_args.due_date,
        priority=_args.priority,
        id=None,  # This will be set after inserting into the database
    )

    task_id = new_task_creator(task)
    print(f"Task added successfully with ID {task_id}.")


def delete_task_handler(_args):
    """Handles the 'delete' command by removing a task by ID or by (scheduled-date AND content)."""
    if _args.id:
        success = delete_task(task_id=_args.id)
    elif _args.schedule_date and _args.content:
        success = delete_task(scheduled_date=_args.schedule_date, content=_args.content)
    else:
        print(
            "Error: Provide either --id OR both --schedule-date and --content to delete a task."
        )
        return

    print("Warning: Prioritize deletion by ID first.")
    print("Warning: Deleting a task will not take the ID back.")

    if success:
        print("Task deleted successfully.")
    else:
        print("Task not found or could not be deleted.")


# CLI setup
parser = argparse.ArgumentParser(description="Task CLI")
subparsers = parser.add_subparsers(dest="command")

# Add 'init' command
init_parser = subparsers.add_parser("init", help="Initialize the system")
init_parser.set_defaults(func=init)

# Add 'reset' command
reset_parser = subparsers.add_parser("reset", help="Reset the system")
reset_parser.set_defaults(func=lambda _args: reset())


# Add 'add' command
add_parser = subparsers.add_parser("add", help="Add a new task")
add_parser.add_argument("content", type=str, help="Task description")
add_parser.add_argument(
    "--schedule-date",
    type=validate_date,
    required=True,
    help="Scheduled date (YYYY-MM-DD)",
)
add_parser.add_argument(
    "--start-date", type=validate_date, required=False, help="Start date (YYYY-MM-DD)"
)
add_parser.add_argument(
    "--due-date", type=validate_date, required=False, help="Due date (YYYY-MM-DD)"
)
add_parser.add_argument(
    "--priority", type=int, choices=range(1, 5), help="Priority level (1-4)"
)
add_parser.set_defaults(func=add_task)

# Add 'delete' command
delete_parser = subparsers.add_parser("delete", help="Delete a task")
delete_parser.add_argument("--id", type=int, help="Task ID")
delete_parser.add_argument(
    "--schedule-date", type=validate_date, help="Scheduled date (YYYY-MM-DD)"
)
delete_parser.add_argument("--content", type=str, help="Task description")
delete_parser.set_defaults(func=delete_task)

# Parse arguments
args = parser.parse_args()
if args.command:
    args.func(args)
else:
    parser.print_help()
