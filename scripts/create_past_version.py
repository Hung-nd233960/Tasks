import tempfile
import os
from typing import Optional
from git import Repo, GitCommandError


def get_last_git_version(file_path: str) -> Optional[str]:
    """
    Given a file path, retrieves the last committed version from Git using GitPython
    and writes it to a temporary file, returning the temp file's path.
    """
    try:
        repo = Repo(os.path.dirname(file_path), search_parent_directories=True)
        rel_path = os.path.relpath(file_path, repo.working_dir)
        blob = repo.head.commit.tree / rel_path
        content = blob.data_stream.read()
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(content)
            temp_file.close()
        return temp_file.name
    except GitCommandError:
        return None
