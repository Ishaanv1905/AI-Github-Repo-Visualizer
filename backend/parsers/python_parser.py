import ast

FRAMEWORK_CALLS = {"Flask", "route", "get", "post", "put", "delete"}

def parse_python_file(file_path: str):
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        tree = ast.parse(f.read())

    functions = []
    classes = []
    imports = []
    calls = []

    # ---- imports & classes (global scan is OK) ----
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            classes.append(node.name)

        elif isinstance(node, ast.Import):
            for n in node.names:
                imports.append(n.name)

        elif isinstance(node, ast.ImportFrom):
            imports.append(node.module)

    # ---- function-level scoped call extraction ----
    for node in tree.body:
        if not isinstance(node, ast.FunctionDef):
            continue

        functions.append(node.name)
        caller = node.name

        # walk ONLY inside function body
        for inner in ast.walk(node):
            if isinstance(inner, ast.Call):

                # foo()
                if isinstance(inner.func, ast.Name):
                    callee = inner.func.id
                    category = (
                        "framework" if callee in FRAMEWORK_CALLS else "business"
                    )

                    calls.append({
                        "caller": caller,
                        "callee": callee,
                        "type": "function",
                        "category": category
                    })

                # obj.method()
                elif isinstance(inner.func, ast.Attribute):
                    callee = inner.func.attr

                    calls.append({
                        "caller": caller,
                        "callee": callee,
                        "object": ast.unparse(inner.func.value),
                        "type": "method",
                        "category": "business"
                    })

    return {
        "functions": functions,
        "classes": classes,
        "imports": imports,
        "calls": calls
    }
