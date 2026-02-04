from backend.core.project_index import ProjectIndex
from backend.core.file_tree import build_file_tree
from backend.core.source_index import build_source_index
from backend.core.entry_points import detect_entry_points
from backend.core.api_index import build_api_index
from backend.parsers.repo_parser import parse_repo
from backend.core.file_dependencies import build_file_dependencies

def analyze_project(project_root: str) -> ProjectIndex:
    index = ProjectIndex(project_root)

    # 1. File tree
    index.file_tree = build_file_tree(project_root)

    # 2. Language stats + source files
    source_index = build_source_index(index.file_tree, project_root)
    index.language_stats = source_index["language_stats"]
    index.source_files = source_index["source_files"]
    
    # 3. Entry points
    for path, meta in index.source_files.items():
        if meta["language"] == "python":
            eps = detect_entry_points(f"{project_root}/{path}")
            index.entry_points.extend(eps)

    # 4. APIs
    index.apis = build_api_index(index.source_files, project_root)

    # 5. Call graph
    parsed = parse_repo(project_root)
    
    for file in parsed:
    # calls
        for call in file.get("calls", []):
            index.calls.append(call)

    # imports (THIS WAS MISSING)
        for imp in file.get("imports", []):
            index.imports.append({
                "file": file.get("file_path"),
                "module": imp
            })
    index.file_dependencies = build_file_dependencies(parsed, project_root)
    return index
