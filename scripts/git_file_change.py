# pylint: disable=C0114

from typing import Dict, List
from git import Repo


def get_repo_file_changes(repo_path: str = ".") -> Dict[str, List[str]]:
    """
    Get the list of changed, newly created, and deleted files in a Git repository.

    Parameters:
        repo_path (str): Path to the Git repository. Defaults to the current directory.

    Returns:
        Dict[str, List[str]]: A dictionary with keys:
            - "changed": List of modified or staged files.
            - "new": List of newly created (untracked) files.
            - "deleted": List of deleted files.
    """
    repo = Repo(repo_path)

    file_changes: Dict = {"changed": [], "new": [], "deleted": []}

    if repo.is_dirty(untracked_files=True):
        # Get changed (modified/staged) files
        diff_index = repo.index.diff(None)
        file_changes["changed"] = [item.a_path for item in diff_index]

        # Get newly created (untracked) files
        file_changes["new"] = repo.untracked_files

        # Get deleted files
        file_changes["deleted"] = [
            item.a_path for item in diff_index if item.change_type == "D"
        ]

    return file_changes


if __name__ == "__main__":
    REPO_PATH = "."  # Current directory
    changes = get_repo_file_changes(REPO_PATH)["changed"]
    added = get_repo_file_changes(REPO_PATH)["new"]
    deleted = get_repo_file_changes(REPO_PATH)["deleted"]
    if changes:
        print("Changed files:")
        for file in changes:
            print(f"- {file}")
    else:
        print("No changes detected.")

    if added:
        print("\nNew files:")
        for file in added:
            print(f"- {file}")

    if deleted:
        print("\nDeleted files:")
        for file in deleted:
            print(f"- {file}")
