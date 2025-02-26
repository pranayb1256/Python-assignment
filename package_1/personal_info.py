class PersonalInfo:
    def __init__(self, name, age, gender, blood_group, height, weight):
        self.name = name
        self.age = age
        self.gender = gender
        self.blood_group = blood_group
        self.height = height
        self.weight = weight

    def display_info(self):
        return (f"Name: {self.name}\n"
                f"Age: {self.age}\n"
                f"Gender: {self.gender}\n"
                f"Blood Group: {self.blood_group}\n"
                f"Height: {self.height}\n"
                f"Weight: {self.weight}")

