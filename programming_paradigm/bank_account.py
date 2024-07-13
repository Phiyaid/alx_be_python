class BankAccount:
    def __init__(self, account_balance = 0):
        self.account_balance =  account_balance
        
        
        
    def deposit(self,amount):
        self.amount = amount + self.account_balance
        return self.amount
    
    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance = self.account_balance - amount 
            return True
        else:
            return False
        
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")
        