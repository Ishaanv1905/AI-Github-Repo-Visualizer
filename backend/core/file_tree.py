LANGUAGE_MAP = {
    ".py": "python",
    ".js": "javascript",
    ".ts": "typescript",
    ".jsx": "javascript",
    ".tsx": "typescript",
    ".java": "java",
    ".cpp": "cpp",
    ".c": "c",
    ".go": "go",
    ".rs": "rust"
}
IGNORE_DIRS = {
    ".git",
    "__pycache__",
    "node_modules",
    "venv",
    ".idea",
    ".vscode",
    "dist",
    "build"
}
from pathlib import Path
from backend.core.file_tree import LANGUAGE_MAP, IGNORE_DIRS

def build_file_tree(root_path: str):
    root = Path(root_path)

    def walk(current: Path):
        if current.name in IGNORE_DIRS:
            return None

        node = {
            "name": current.name,
            "type": "directory" if current.is_dir() else "file",
            "path": str(current.relative_to(root)),
            "children": []
        }

        if current.is_file():
            node["extension"] = current.suffix
            node["size (bytes)"] = current.stat().st_size
            node["language"] = LANGUAGE_MAP.get(current.suffix)

            return node

        for child in sorted(current.iterdir(), key=lambda x: (x.is_file(), x.name)):
            child_node = walk(child)
            if child_node:
                node["children"].append(child_node)

        return node

    return walk(root)
