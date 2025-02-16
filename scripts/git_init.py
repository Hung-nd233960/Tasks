import os
from git import Repo


def initialize_git_repo():
    """Initializes a Git repository if one does not exist and makes an initial commit."""
    if not os.path.exists(".git"):
        repo = Repo.init(".")
        print("Initialized a new Git repository.")

        # Stage all files
        repo.index.add([".gitignore", "tasks", "notes", "db"])

        # Make an initial commit
        repo.index.commit("Initial commit: Setup project structure")
        print("Initial commit created.")

    else:
        print("Git repository already exists.")


# Run setup
initialize_git_repo()
