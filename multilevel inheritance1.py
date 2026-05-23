'''Write a Python program to demonstrate multi-level inheritance
using three classes: Department, Course, and Student.'''
class Department:
    def getdeptdetails(self):
        self.dept_id = input("Enter Department ID: ")
        self.dept_name = input("Enter Department Name: ")

    def printdept(self):
        print("\n--- Department Details ---")
        print("ID:",self.dept_id)
        print("Name:",self.dept_name)

class Course(Department):
    def getcourse(self):
        print()
        self.course_code = input("Enter Course Code: ")
        self.course_name = input("Enter Course Name: ")
        self.duration = input("Enter Course Duration: ")

    def printcourse(self):
        print("\n--- Course Details ---")
        print("Code:",self.course_code)
        print("Name:",self.course_name)
        print("Duration:",self.duration)

class Student(Course):
    def getdetails(self):
        self.getdeptdetails()
        self.getcourse()
        print()
        self.rollno = input("Enter Student Roll No: ")
        self.sname = input("Enter Student Name: ")
        self.mark = input("Enter Student Marks: ")

    def printstudent(self):
        self.printdept()
        self.printcourse()
        print("\n--- Student Details ---")
        print("Roll No:",self.rollno)
        print("Student Name:",self.sname)
        print("Marks:",self.mark)
s = Student()
s.getdetails()
s.printstudent()
