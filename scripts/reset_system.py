import os
import shutil
from init_system import init


# Reset the project to its initial state
def reset():
    db_file = "db/tasks.db"
    tasks_dir = "tasks"
    if os.path.exists(db_file):
        os.remove(db_file)
    if os.path.exists(tasks_dir):
        shutil.rmtree(tasks_dir)
        os.makedirs(tasks_dir, exist_ok=True)
    init()
    print("Project has been reset to its initial state.")


if __name__ == "__main__":
    reset()
