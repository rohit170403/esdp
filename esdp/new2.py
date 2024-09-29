class Bank:
    def __init__(self, name, accNo, type, balance):
        self.name = name
        self.accNo = accNo
        self.type = type
        self.balance = balance

    def display(self):
        print("Name:", self.name, "Balance:", self.balance)

    def deposit(self):
        amount = int(input("Enter Value : "))
        self.balance += amount
        print("Current Amount:", self.balance)

    def withdraw(self):
        amount = int(input("Enter Value : "))
        self.balance -= amount
        print("Current Amount:", self.balance)


sbi = Bank("Jayesh", 123456, "saving", 500)
sbi.display()
# sbi.deposit()
sbi.withdraw()


