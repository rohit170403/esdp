class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        return f"{self.name} is working."

    def getSalary(self):
        return f"{self.name}'s salary is ${self.salary}"


class HRManager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
        self.employees = []

    def work(self):
        return f"{self.name} is managing HR tasks."

    def addEmployee(self, employee):
        if isinstance(employee, Employee):
            self.employees.append(employee)
            return f"{employee.name} has been added to HR manager's team."
        else:
            return "Invalid employee object. Cannot add to the team."


# Example usage:
employee1 = Employee("John", 50000)
employee2 = Employee("Alice", 60000)
hr_manager = HRManager("Emma", 80000)

print(employee1.work())
print(employee2.getSalary())
print(hr_manager.work())
print(hr_manager.addEmployee(employee1))
print(hr_manager.addEmployee("Invalid Employee"))  
