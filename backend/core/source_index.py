def count_lines(file_path: str):
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            return sum(1 for _ in f)
    except Exception:
        return 0

from collections import defaultdict
from pathlib import Path

def build_source_index(file_tree: dict, project_root: str):
    language_stats = defaultdict(lambda: {"files": 0, "lines": 0})
    source_files = {}

    def walk(node):
        if node["type"] == "file" and node.get("language"):
            path = node["path"]
            abs_path = Path(project_root) / path
            lines = count_lines(abs_path)

            source_files[path] = {
                "language": node["language"],
                "size": node.get("size", 0),
                "lines": lines
            }

            lang = node["language"]
            language_stats[lang]["files"] += 1
            language_stats[lang]["lines"] += lines

        for child in node.get("children", []):
            walk(child)

    walk(file_tree)

    return {
        "language_stats": dict(language_stats),
        "source_files": source_files
    }
