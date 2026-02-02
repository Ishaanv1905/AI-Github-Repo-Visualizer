from pathlib import Path
from backend.parsers.python_parser import parse_python_file

IGNORE_DIRS = {"venv", "__pycache__", ".git"}

def parse_repo(repo_path: str):
    repo_path = Path(repo_path)
    results = []

    for path in repo_path.rglob("*.py"):
        if any(part in IGNORE_DIRS for part in path.parts):
            continue

        file_result = parse_python_file(str(path))
        file_result["file_path"] = str(path)
        results.append(file_result)

    return results
