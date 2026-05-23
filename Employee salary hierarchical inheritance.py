'''Write Python code to implement the Employee, Manager, and
Developer class hierarchy to represent different types of employees in
a company. The base class is Employee, which has attributes name and
salary, and a method calculate_bonus that calculates the bonus based
on the bonus percentage.'''
class Employee:
    def get_emp_details(self):
        self.id = input("Enter employee id:")
        self.name = input("Enter employee name:")
        self.salary = float(input("Enter salary:"))

    def calculate_bonus(self):
        print("----Calculating Bonus----")
        self.percentage = float(input("Enter bonus percentage:"))
        bonus=self.salary * (self.percentage / 100)
        print("Bonus:Rs.",bonus)

class Manager(Employee):
    def manager_details(self):
        self.department = input("Enter department:")
        self.team_size = int(input("Enter team size:"))
        self.allowance = input("Enter allowance:Rs.")

    def printManager(self):
        print("Manager:",self.name,"\nDepartment:",self.department)
        print("Team size:",self.team_size,"\nAllowance:Rs.",self.allowance)
        self.calculate_bonus()
        
class Developer(Employee):
    def developer_details(self):
        self.project = input("Enter project name:")
        self.experience = input("Enter years of experience:")

    def printDeveloper(self):
        print("Developer:",self.name,"\nProject name:",self.project,"\nExperience:",self.experience)
        self.calculate_bonus()

while True:
    typ=input("\nEnter employee type(Manager/Developer) or [type exit to exit page]:")
    if typ=='Manager':
        mgr = Manager()                         #101, "Alice", 80000, 10, "IT", 5, 5000
        mgr.get_emp_details()
        mgr.manager_details()
        print("---Manager details---")
        mgr.printManager()
    elif typ=='Developer':
        dev = Developer()                      #102, "Bob", 60000, 5, "E-commerce", 3
        dev.get_emp_details()
        dev.developer_details()
        print("---Developer details---")
        dev.printDeveloper()
    elif typ.upper()=='EXIT':
        print("Exiting....")
        break
    else:
        print("Not manager or developer")
