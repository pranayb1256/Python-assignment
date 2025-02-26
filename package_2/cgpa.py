class Cgpa:
    def __init__(self, sem1, sem2, sem3):  # Fixed variable names
        self.sem1 = sem1
        self.sem2 = sem2
        self.sem3 = sem3

    def display_cgpa(self):  # Renamed method to match functionality
        return f"Sem-I: {self.sem1}, Sem-II: {self.sem2}, Sem-III: {self.sem3}"
