"""
Retrieves a list of changed files from a Git repository, including modified,
staged, and untracked files.
Parameters:
    repo_path (str): The path to the repository root directory. Defaults to the
                     current directory ('.').
Returns:
    list: A list of file paths representing changed or untracked files in the
          repository.
"""

from git import Repo


# pylint: disable=C0116
def get_changed_files(repo_path="."):
    repo = Repo(repo_path)
    changed_files = []

    if repo.is_dirty(untracked_files=True):
        diff_index = repo.index.diff(None)
        changed_files = [item.a_path for item in diff_index]

        # Include untracked files
        untracked_files = repo.untracked_files
        changed_files.extend(untracked_files)

    return changed_files


if __name__ == "__main__":
    REPO_PATH = "."  # Current directory
    changes = get_changed_files(REPO_PATH)

    if changes:
        print("Changed files:")
        for file in changes:
            print(f"- {file}")
    else:
        print("No changes detected.")
