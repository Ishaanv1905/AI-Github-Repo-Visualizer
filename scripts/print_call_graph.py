from backend.parsers.repo_parser import parse_repo

data = parse_repo("backend")

print("\nCALL GRAPH\n")
for file in data:
    for call in file.get("calls", []):
        print(f"{call['caller']}  -->  {call['callee']} ({call['type']})")
