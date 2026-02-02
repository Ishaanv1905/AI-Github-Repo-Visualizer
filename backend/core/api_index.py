import ast
from backend.core.route_detector import extract_apis_from_function

def build_api_index(source_files: dict, project_root: str):
    apis = []

    for path, meta in source_files.items():
        if meta["language"] != "python":
            continue

        abs_path = f"{project_root}/{path}"

        try:
            with open(abs_path, "r", encoding="utf-8", errors="ignore") as f:
                tree = ast.parse(f.read())
        except Exception:
            continue

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                apis.extend(extract_apis_from_function(node, path))

    return apis
