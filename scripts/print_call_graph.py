from backend.parsers.repo_parser import parse_repo

data = parse_repo("test_project/simple_flask_app")

print("\nCALL GRAPH\n")
for file in data:
    for call in file.get("calls", []):
        print(f"{call['caller']}  -->  {call['callee']} ({call['type']})")
