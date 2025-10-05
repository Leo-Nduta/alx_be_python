class BankAccount:
    def _init_ (self,initial_balance = 0):
        self.account_balance = initial_balance
    
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