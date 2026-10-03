class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self,amount):
        """ we can put some checks here"""
        self.balance +=amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def __str__(self):
        return str(self.balance)

    

account = BankAccount(500)
print(account.withdraw(600)) 