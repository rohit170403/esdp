class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited amount is {amount} and balance is {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawn {amount} and New balance: {self.balance}")
        else:
            print("Insufficienct balalnce here")
            
class SavingAccount(BankAccount):
    def withdraw(self, amount):
        if self.balance - amount < 1000:
            print("sorry minimum balance of 1000 required.")
        else:
            super().withdraw(amount)
             
   
ac = SavingAccount()
while(True):
    print("1. Deposits")
    print("2. Withdraw")
    print("3. balance check")
    print("4. exit here")
    choice = int(input("Enter your choice = "))
    if choice == 1:
        c = int(input("Enter amount = "))
        ac.deposit(c)
        
    elif choice == 2:
        c = int(input("Enter amount = "))
        ac.withdraw(c)
        
    elif choice == 3:
        print(f"Your balalnce is {ac.balance}")
    
    elif choice ==4 :
        print("Stop")
        break;

    else :
        print("Invalid choice")
        break;