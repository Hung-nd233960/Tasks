# pylint: disable=missing-module-docstring, missing-function-docstring
import os
from init.db_init import init_db
from init.git_init import initialize_git_repo

# Initialize the database and Git repository


def setup_project_structure():
    """Creates the required project directories and a .gitignore file."""
    directories = ["tasks", "notes", "db"]

    for directory in directories:
        os.makedirs(directory, exist_ok=True)

    gitignore_content = """

# Ignore compiled Python files
__pycache__/
.mypy_cache/
.venv/
.vscode/
*.pyc
*.pyo

# Ignore temporary or log files
*.log
*.tmp
*.swp
    
    """

    with open(".gitignore", "w", encoding="utf-8") as file:
        file.write(gitignore_content)

    print("Project directories and .gitignore file have been set up.")
    print("Next, initialize the database and Git repository.")


# Run setup


def init():
    setup_project_structure()
    init_db()
    initialize_git_repo()
    print("Project setup complete.")


if __name__ == "__main__":
    init()
