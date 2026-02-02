import ast
from backend.core.api_model import make_api

HTTP_METHOD_MAP = {
    "get": "GET",
    "post": "POST",
    "put": "PUT",
    "delete": "DELETE",
    "patch": "PATCH",
    "route": None,   # Flask generic route
}

def extract_apis_from_function(func_node, file_path: str):
    apis = []

    for decorator in func_node.decorator_list:
        if not isinstance(decorator, ast.Call):
            continue

        if isinstance(decorator.func, ast.Attribute):
            dec_name = decorator.func.attr.lower()

            if dec_name in HTTP_METHOD_MAP:
                # path
                if not decorator.args:
                    continue
                if not isinstance(decorator.args[0], ast.Constant):
                    continue

                path = decorator.args[0].value

                # method
                method = HTTP_METHOD_MAP[dec_name]
                framework = "fastapi" if dec_name != "route" else "flask"

                # Flask: methods=["POST"]
                if dec_name == "route":
                    method = "GET"
                    for kw in decorator.keywords:
                        if kw.arg == "methods" and isinstance(kw.value, (ast.List, ast.Tuple)):
                            if kw.value.elts and isinstance(kw.value.elts[0], ast.Constant):
                                method = kw.value.elts[0].value

                apis.append(
                    make_api(
                        method=method,
                        path=path,
                        handler=func_node.name,
                        file=file_path,
                        framework=framework
                    )
                )

    return apis
