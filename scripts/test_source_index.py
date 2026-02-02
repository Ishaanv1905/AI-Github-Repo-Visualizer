from backend.core.file_tree import build_file_tree
from backend.core.source_index import build_source_index
import json

tree = build_file_tree("backend")
index = build_source_index(tree, "backend")

print(json.dumps(index, indent=2))
