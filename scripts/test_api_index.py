from backend.core.file_tree import build_file_tree
from backend.core.source_index import build_source_index
from backend.core.api_index import build_api_index
import json

ROOT = "test_project/simple_flask_app"

tree = build_file_tree(ROOT)
index = build_source_index(tree, ROOT)

apis = build_api_index(index["source_files"], ROOT)

print(json.dumps(apis, indent=2))
