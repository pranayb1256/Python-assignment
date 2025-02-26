class College:
    def __init__(self, name, city, Affilated_Univ, Branch, Department, Duration):
        self.college_name = name
        self.city=city
        self.Affilated_Univ = Affilated_Univ
        self.Branch = Branch
        self.Department = Department
        self.Duration = Duration

    def get_name(self):
        return f"{self.college_name}, {self.city}, {self.Affilated_Univ}, {self.Branch}, {self.Department}, {self.Duration}"