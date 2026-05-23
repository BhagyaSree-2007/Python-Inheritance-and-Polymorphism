'''The student classes contain the data members name, roll number and
test marks. There exists a Literary_Student class which represents a
student in literary association with data members marks which
represents marks of literary association participation. There also exists
a class Sports_Student class which represents a student participating in
sports and contains the data member called sports mark. The class
Lit_sport_student represents a student who participates in both. Write
a Python program to represent the above class hierarchy, create
objects and calculate the total marks polymorphically.'''
class Student:
    def get_details(self):
        self.name = input("Enter name:")
        self.roll_no = input("Enter rollno:")
        self.test_marks = float(input("Enter test marks:"))

    def total_marks(self):
        return self.test_marks

    def display(self):
        print("Name:",self.name,"\nRoll No:",self.roll_no,"\nTest Marks:",self.test_marks)

class Literary_Student(Student):
    def get_literary(self):
        self.literary_marks =float(input("Enter literary marks:"))

    def total_marks(self):
        return super().total_marks() + self.literary_marks

    def display(self):
        super().display()
        print("Literary Marks:",self.literary_marks)

class Sports_Student(Student):
    def get_sport(self):
        self.sports_marks =float(input("Enter sports marks:"))

    def total_marks(self):
        return super().total_marks() + self.sports_marks

    def display(self):
        super().display()
        print("Sports Marks:",self.sports_marks)

class Lit_Sport_Student(Literary_Student, Sports_Student):
    def total_marks(self):
        return self.test_marks + self.literary_marks + self.sports_marks

    def display(self):
        print()
        Student.display(self)
        print("Literary Marks:",self.literary_marks)
        print("Sports Marks:",self.sports_marks)
        print("Total Marks:",self.total_marks())

st=Lit_Sport_Student()
st.get_details()
st.get_sport()
st.get_literary()
st.display()
