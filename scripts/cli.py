"""
This module defines a command-line interface (CLI) for managing tasks with two primary commands:
- init: Initializes the system.
- add: Adds a new task.
Functions:
----------
validate_date(date_str):
    Validates that the provided date string follows the YYYY-MM-DD format.
    Returns a datetime.date object if valid, or raises an argparse.ArgumentTypeError if invalid.
add_task(_args):
    Creates and stores a new task using TaskDetails. Defaults the task status to "undone",
    sets the other attributes (content, schedule date, start date, due date, and priority)
    based on user input, and prints a confirmation message with the generated task ID.
Command-line Usage:
-------------------
Run 'python cli.py' followed by the desired command and corresponding arguments.
For example:
    python cli.py add "Complete report" --schedule-date 2023-10-05
"""

import argparse
import datetime
from func.model import TaskDetails
from new_task_creator import new_task_creator


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


# CLI setup
parser = argparse.ArgumentParser(description="Task CLI")
subparsers = parser.add_subparsers(dest="command")

# Add 'init' command
init_parser = subparsers.add_parser("init", help="Initialize the system")
init_parser.set_defaults(func=lambda args: print("Initializing..."))

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

# Parse arguments
args = parser.parse_args()
if args.command:
    args.func(args)
else:
    parser.print_help()
