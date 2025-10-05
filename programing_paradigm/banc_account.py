class BankAccount:
    def __init__ (self,account_balance = 0):
        self.account_balance = account_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False
        
    def display_balance(self):
        return ("Your current bank account balance is " + str(self.account_balance))