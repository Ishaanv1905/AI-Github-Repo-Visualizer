from backend.core.file_tree import build_file_tree
import json

tree = build_file_tree("test_project/simple_flask_app")

print(json.dumps(tree, indent=2))
