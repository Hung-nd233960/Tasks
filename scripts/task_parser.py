"""
Parse a string representing a task line and extract task details.
This function searches for a task marker of the form:
    - [x or space] #task <content> [scheduled:: YYYY-MM-DD] [start:: YYYY-MM-DD]
    [end:: YYYY-MM-DD] [priority:: <number>] [id:: <number>]
Parameters:
    line (str): A line of text representing a task to be parsed.
Returns:
    dict or None: A dictionary with the following keys if the line matches:
        - "status" (str): "done" if marked with [x], otherwise "undone".
        - "content" (str): The main text of the task.
        - "scheduled_date" (str or None): Scheduled date in 'YYYY-MM-DD' format.
        - "start_date" (str or None): Start date in 'YYYY-MM-DD' format.
        - "end_date" (str or None): End date in 'YYYY-MM-DD' format.
        - "priority" (int or None): Priority level extracted from the line.
        - "id" (int or None): Unique task identifier.
    Returns None if the line does not match the task pattern.
"""

# pylint: disable= C0116, C0115
import re
from datetime import datetime
from typing import Optional
from scripts.func.model import TaskDetails

# TaskParser function to parse task lines


def parse_task_line(line: str) -> Optional[TaskDetails]:
    task_pattern = (
        r"- \[([ x])\]\s+#task\s+(.*?)"  # Status and content
        r"(?:\s+\[scheduled::\s*(\d{4}-\d{2}-\d{2})\])?"  # Scheduled date
        r"(?:\s+\[start::\s*(\d{4}-\d{2}-\d{2})\])?"  # Start date
        r"(?:\s+\[due::\s*(\d{4}-\d{2}-\d{2})\])?"  # Due date
        r"(?:\s+\[priority::\s*(\d+)\])?"  # Priority
        r"(?:\s+\[id::\s*(\d+)\])?"  # ID
        r"\s*$"  # End of line to ensure clean matching
    )

    match = re.search(task_pattern, line)
    print(match)  # Debugging the match object

    if match:
        scheduled_str = match.group(3)
        start_str = match.group(4)
        due_str = match.group(5)

        try:
            scheduled_date = (
                datetime.strptime(scheduled_str, "%Y-%m-%d") if scheduled_str else None
            )
        except ValueError:
            scheduled_date = None

        try:
            start_date = datetime.strptime(start_str, "%Y-%m-%d") if start_str else None
        except ValueError:
            start_date = None

        try:
            due_date = datetime.strptime(due_str, "%Y-%m-%d") if due_str else None
        except ValueError:
            due_date = None

        return {
            "status": "done" if match.group(1) == "x" else "undone",
            "content": match.group(2),
            "scheduled_date": scheduled_date,
            "start_date": start_date,
            "due_date": due_date,
            "priority": int(match.group(6)) if match.group(6) else None,
            "id": int(match.group(7)) if match.group(7) else None,
        }
    return None


# Example usage
if __name__ == "__main__":
    EXAMPLE_LINE = "- [ ] #task Finish the report [scheduled:: 2025-03-01]  [start:: 2025-02-15]  [due:: 2025-02-28]  [priority:: 2]  [id:: 123]"
    parsed_task = parse_task_line(EXAMPLE_LINE)
    print(parsed_task)
