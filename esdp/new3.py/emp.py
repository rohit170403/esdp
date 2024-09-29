class Emp:
    def work(self):
        print("Employee is working...")

    def getsal(self):
        print("Your salary is...")

class HRman(Emp):
    def work(self):
        print("HR Manager is working...")

    def addEmp(self):
        print("Adding an employee...")

# Example usage:
employee = Emp()
hr_manager = HRman()

employee.work()
employee.getsal()

hr_manager.work()
hr_manager.addEmp()

