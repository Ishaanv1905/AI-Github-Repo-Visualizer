import ast

def detect_main_block(tree):
    for node in ast.walk(tree):
        if isinstance(node, ast.If):
            if (
                isinstance(node.test, ast.Compare)
                and isinstance(node.test.left, ast.Name)
                and node.test.left.id == "__name__"
            ):
                return True
    return False
def detect_route_decorators(func_node):
    routes = []

    for decorator in func_node.decorator_list:
        if isinstance(decorator, ast.Call):
            if isinstance(decorator.func, ast.Attribute):
                name = decorator.func.attr
                if name in {"route", "get", "post", "put", "delete"}:
                    if decorator.args:
                        if isinstance(decorator.args[0], ast.Constant):
                            routes.append(decorator.args[0].value)

    return routes
def detect_entry_points(file_path: str):
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        tree = ast.parse(f.read())

    entry_points = []

    # Type A: __main__
    if detect_main_block(tree):
        entry_points.append({
            "type": "script",
            "file": file_path
        })

    # Type C: route handlers
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            routes = detect_route_decorators(node)
            for route in routes:
                entry_points.append({
                    "type": "route",
                    "file": file_path,
                    "function": node.name,
                    "route": route
                })

    return entry_points
