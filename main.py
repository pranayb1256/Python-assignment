# Import classes from the packages
from package_1 import Liking, PersonalInfo, Residence
from package_2 import Cgpa, College, Skills

# Create an instance of PersonalInfo
person_info = PersonalInfo(name="Pranay Bhoir",
                           age=20, gender="Male",
                           blood_group="O+",
                           height="6'1",
                           weight="90kg")

# Create an instance of Residence
residence_info = Residence(city="Dombivli",
                           country="India",
                           postal_code="421204",
                           street="Lodha-Heaven",
                           state="Maharashtra")

# Create an instance of Liking
person1 = Liking(
    favorite_food=["Biriyani", "Butter Chicken"],
    football_team="Man City",
    books=["Zero to One", "Atomic Habits"],
    anime=["Bleach", "Dr. Stone"],
    favorite_place="Kashmir"
)

# Create an instance of Cgpa
person_cgpa = Cgpa(sem1="9.17",
                   sem2="8.17",
                   sem3="9.75")

# Create an instance of College
person_college = College("Lokmanya Tilak College of Engineering",
                         "Navi Mumbai",
                         "University of Mumbai",
                         "Computer Engineering",
                         "Artificial Intelligence and Machine Learning",
                         "2023-2027")

# Create an instance of Skills
person_skills = Skills(["Python", "JavaScript", "C++"],
                       ["Django", "React", "Node.js"],
                       ["MySQL", "MongoDB"],
                       ["VS Code", "PyCharm", "Postman", "Git", "GitHub", "Docker"])

# Display outputs
print(person1.display_liking(), end="\n\n")
print(person_info.display_info(), end="\n\n")
print(residence_info.display_residence(), end="\n\n")
print(person_cgpa.display_cgpa(), end="\n\n")
print(person_college.get_name(), end="\n\n")
print(person_skills.display_skills(), end="\n\n")
