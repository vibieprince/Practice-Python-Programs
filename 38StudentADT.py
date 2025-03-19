class Student:
    def __init__(self, name, roll_no, grade):
        """Constructor to initialize student details"""
        self.name = name
        self.roll_no = roll_no
        self.grade = grade

    def set_name(self, name):
        """Set the name of the student"""
        self.name = name

    def get_name(self):
        """Get the name of the student"""
        return self.name

    def set_roll_no(self, roll_no):
        """Set the roll number of the student"""
        self.roll_no = roll_no

    def get_roll_no(self):
        """Get the roll number of the student"""
        return self.roll_no

    def set_grade(self, grade):
        """Set the grade of the student"""
        self.grade = grade

    def get_grade(self):
        """Get the grade of the student"""
        return self.grade

    def display_info(self):
        """Display the student information"""
        print(f"Student Name: {self.name}")
        print(f"Roll Number: {self.roll_no}")
        print(f"Grade: {self.grade}")

# Creating an object of Student ADT
student1 = Student("Prince", 101, "A")

# Displaying student information
student1.display_info()

# Modifying student information
student1.set_grade("A+")
print("\nAfter updating grade:")
student1.display_info()
