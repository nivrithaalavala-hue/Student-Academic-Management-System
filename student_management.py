from datetime import date

class Student:
    TOTAL_FEE = 100000   # assumed total college fee

    def __init__(self, student_id, name, marks, dob, fee_paid):
        self.student_id = student_id
        self.name = name
        self.marks = marks
        self.dob = dob
        self.fee_paid = fee_paid

    # Calculate Average Marks
    def calculate_average(self):
        return sum(self.marks) / len(self.marks)

    # Calculate CGPA
    def calculate_cgpa(self):
        avg = self.calculate_average()
        return round(avg / 10, 2)

    # Calculate Age
    def calculate_age(self):
        today = date.today()
        birth_year, birth_month, birth_day = map(int, self.dob.split("-"))
        birth_date = date(birth_year, birth_month, birth_day)
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age

    # Calculate Fee Balance
    def calculate_fee_balance(self):
        return Student.TOTAL_FEE - self.fee_paid

    # Display Student Details
    def display_details(self):
        print("\nStudent ID:", self.student_id)
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Average:", round(self.calculate_average(), 2))
        print("CGPA:", self.calculate_cgpa())
        print("Age:", self.calculate_age())
        print("Fee Balance:", self.calculate_fee_balance())


class College:
    def __init__(self, code, name, location):
        self.code = code
        self.name = name
        self.location = location
        self.students = []

    # Register Student
    def register_student(self, student):
        self.students.append(student)

    # Display College and Student Report
    def display_report(self):
        print("\n===== College Details =====")
        print("College Code:", self.code)
        print("College Name:", self.name)
        print("Location:", self.location)

        print("\n===== Student Academic Report =====")
        for student in self.students:
            student.display_details()


# Main Program
college = College("C101", "ABC Engineering College", "Hyderabad")

s1 = Student("S001", "Rahul", [85, 78, 90], "2003-05-14", 70000)
s2 = Student("S002", "Ananya", [88, 92, 80], "2004-02-10", 85000)
s3 = Student("S003", "Kiran", [75, 70, 82], "2003-11-25", 60000)

college.register_student(s1)
college.register_student(s2)
college.register_student(s3)

college.display_report()
