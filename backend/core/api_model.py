def make_api(
    *,
    method: str,
    path: str,
    handler: str,
    file: str,
    framework: str
):
    return {
        "method": method,
        "path": path,
        "handler": handler,
        "file": file,
        "framework": framework,
        "entry_type": "http"
    }
