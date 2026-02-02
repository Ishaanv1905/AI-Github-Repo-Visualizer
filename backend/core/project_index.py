class ProjectIndex:
    def __init__(self, root: str):
        self.root = root

        self.file_tree = None
        self.language_stats = {}
        self.source_files = {}
        self.entry_points = []
        self.apis = []
        self.calls = []
        self.file_dependencies = []


    def to_dict(self):
        return {
            "root": self.root,
            "languages": self.language_stats,
            "entry_points": self.entry_points,
            "apis": self.apis,
            "calls": self.calls,
            "file_dependencies": self.file_dependencies,
            "source_files_count": len(self.source_files)
        }
