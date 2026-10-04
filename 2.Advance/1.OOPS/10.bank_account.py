class BankAccount:
    def __init__(self, balance:int =0):
        self.balance = balance

    def deposit(self,amount:int) -> str:
        """ we can put some checks here"""
        print("i'm from parent class")
        self.balance +=amount
        return f"Deposited: {amount}. New balance: {self.balance}"

    def withdraw(self, amount:int) -> str:
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrawn: {amount}. New balance: {self.balance}"
        return "Insufficient funds"

    def __str__(self):
        return str(self.balance)
    
class MinimumBalanceAccount(BankAccount):
    def __init__(self, balance:int =1000, minimum_balance:int = 500):
        super().__init__(balance)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount:int) -> str: # overridden method - we are changing the functionality of withdraw method in child class
        if self.balance - amount >= self.minimum_balance:
            return super().withdraw(amount) # calling the withdraw method of parent class
        else:
            return f"Cannot withdraw {amount}. Minimum balance of {self.minimum_balance} must be maintained. Current balance: {self.balance}"

    """ we can remove these below function cuz its inheriting from parent class and 
    we are not changing the functionality of these methods in child class. 
    but if we want to change the functionality of these methods in child class then 
    we can override these methods in child class. """
    # def deposit(self,amount:int) -> str:   # even if we dont hve this function in clhild class we can invoke this function with child class object.
    #     print("i'm from child class")
    #     self.balance +=amount
    #     return f"Deposited: {amount}. New balance: {self.balance}"

    # def __str__(self):   # No needed to override this method in child class as it is already defined in parent class and we are not changing the functionality of this method in child class.
    #     return str(self.balance)


minaccount = MinimumBalanceAccount(1000, 400)
# print(minaccount)
print(minaccount.withdraw(700)) 