from pathlib import Path

def resolve_import_to_file(import_name: str, project_root: str):
    """
    services.auth_service -> services/auth_service.py
    """
    parts = import_name.split(".")
    candidate = Path(project_root).joinpath(*parts)

    # Try module.py
    py_file = candidate.with_suffix(".py")
    if py_file.exists():
        return str(py_file.relative_to(project_root))

    # Try package/__init__.py
    init_file = candidate / "__init__.py"
    if init_file.exists():
        return str(init_file.relative_to(project_root))

    return None
def build_file_dependencies(parsed_files: list, project_root: str):
    dependencies = []

    for file_data in parsed_files:
        source_file = file_data.get("file_path")
        imports = file_data.get("imports", [])

        if not source_file:
            continue

        # normalize path
        source_file = source_file.replace("\\", "/")

        for imp in imports:
            if not imp:
                continue

            target = resolve_import_to_file(imp, project_root)
            if target:
                dependencies.append({
                    "from": source_file,
                    "to": target,
                    "type": "import"
                })

    return dependencies
