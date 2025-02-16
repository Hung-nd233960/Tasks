"""
Initialize an SQLite database for task management.
This function creates a directory, if it does not already exist, to hold
the database file. It then connects to or creates the specified database
file and sets up a 'tasks' table if it does not already exist.
Args:
    db_name (str): Optional name of the SQLite database file. Defaults to 'tasks.db'.
Returns:
    None
"""

# pylint: disable=C0116
import sqlite3
import os


def init_db(db_name="tasks.db"):
    db_path = os.path.join("db", db_name)
    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create the tasks table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL,
            start_date TEXT,
            due_date TEXT,
            scheduled_date TEXT,
            created_date TEXT DEFAULT (datetime('now')),
            modified_date TEXT DEFAULT (datetime('now')),
            priority INTEGER DEFAULT 3,
            status TEXT DEFAULT 'undone',
            hash TEXT UNIQUE NOT NULL
        )
    """
    )

    # Create an index on important fields for faster querying
    cursor.execute(
        """
        CREATE INDEX IF NOT EXISTS idx_tasks_dates 
        ON tasks (start_date, due_date, scheduled_date, modified_date);
        """
    )
    cursor.execute(
        """
        CREATE INDEX IF NOT EXISTS idx_task_hash ON tasks (hash)
        """
    )

    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db()
    print("Database initialized and tasks table created in db/tasks.db.")
