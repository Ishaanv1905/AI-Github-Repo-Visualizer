def print_file_tree(node, indent=0):
    prefix = "│   " * (indent - 1) + ("├── " if indent > 0 else "")
    print(prefix + node["name"])

    for child in node.get("children", []):
        print_file_tree(child, indent + 1)
