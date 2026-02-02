import ast

def parse_python_file(file_path: str):
    with open(file_path, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read())

    functions = []
    classes = []
    imports = []
    calls = []

    current_function = None

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            current_function = node.name
            functions.append(node.name)

        elif isinstance(node, ast.ClassDef):
            classes.append(node.name)

        elif isinstance(node, ast.Import):
            for n in node.names:
                imports.append(n.name)

        elif isinstance(node, ast.ImportFrom):
            imports.append(node.module)

        elif isinstance(node, ast.Call) and current_function:
    # foo()
            if isinstance(node.func, ast.Name):
                calls.append({
                    "caller": current_function,
                    "callee": node.func.id,
                    "type": "function"
                })

        # obj.method()
            elif isinstance(node.func, ast.Attribute):
                calls.append({
                    "caller": current_function,
                    "callee": node.func.attr,
                    "object": ast.unparse(node.func.value),
                    "type": "method"
                })

    return {
        "functions": functions,
        "classes": classes,
        "imports": imports,
        "calls": calls
    }
