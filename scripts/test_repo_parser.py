from backend.parsers.repo_parser import parse_repo

data = parse_repo("test_project/simple_flask_app")
print(data)
