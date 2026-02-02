from backend.core.file_tree import build_file_tree
from backend.core.source_index import build_source_index
from backend.core.entry_points import detect_entry_points

tree = build_file_tree("test_project/simple_flask_app")
index = build_source_index(tree, "test_project/simple_flask_app")

all_entry_points = []

for path, meta in index["source_files"].items():
    if meta["language"] == "python":
        eps = detect_entry_points(f"test_project/simple_flask_app/{path}")
        all_entry_points.extend(eps)

for ep in all_entry_points:
    print(ep)
