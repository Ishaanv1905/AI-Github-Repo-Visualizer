from backend.core.analyze_project import analyze_project
from backend.core.tree_printer import print_file_tree

def print_section(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

project = analyze_project("test_project/simple_flask_app")

print_section("PROJECT ROOT")
print(project.root)

print_section("FILE TREE(HUMAN VIEW)")
print_file_tree(project.file_tree)

import json

print_section("FILE TREE (RAW JSON)")
print(json.dumps(project.file_tree, indent=2))


print_section("LANGUAGES")
for lang, stats in project.language_stats.items():
    print(f"- {lang}: {stats['files']} files, {stats['lines']} lines")

print_section("ENTRY POINTS")
for ep in project.entry_points:
    print(ep)

print_section("BACKEND APIs")
for api in project.apis:
    print(f"[{api['method']}] {api['path']} -> {api['handler']} ({api['file']})")

print_section("CALL GRAPH (edges)")
for call in project.calls:
    print(f"{call['caller']} -> {call['callee']} ({call['type']})")

print_section("FILE-LEVEL DEPENDENCIES")
for dep in project.file_dependencies:
    print(f"{dep['from']}  -->  {dep['to']}")