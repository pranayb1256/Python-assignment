class Skills:
    def __init__(self, Progamming_language, Frameworks, Database, Tools):
        # Ensure input is a list, if not, convert it
        self.Progamming_language = Progamming_language if isinstance(Progamming_language, list) else [Progamming_language]
        self.Frameworks = Frameworks if isinstance(Frameworks, list) else [Frameworks]
        self.Database = Database if isinstance(Database, list) else [Database]
        self.Tools = Tools if isinstance(Tools, list) else [Tools]

    def display_skills(self):
        return (
            f"Programming Languages: {', '.join(self.Progamming_language)}\n"
            f"Frameworks: {', '.join(self.Frameworks)}\n"
            f"Database: {', '.join(self.Database)}\n"
            f"Tools: {', '.join(self.Tools)}"
        )
