class Employee():
    def work(self):
        print("Employee work..")
    def getSalary(self):
        pass
class HR():
    def __init__(self,salary):
        self.salary = salary
    def work(self):
        #super().work()
        print("HR work..") 
    def addEmployee(self):
        print("salary is : ",self.salary)
        print("Employing is adding...")
obj=HR(10000)
obj.work()
obj.addEmployee()