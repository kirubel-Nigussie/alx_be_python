class BankAccount:
    def __init__(self , account_balance = 0) :
        self.account_balance = account_balance
        
def deposit(self, amount):
    self.account_balance += amount 
    return f"Deposited: ${self.account_balance}" 
def withdraw(self,amount):
    if (amount< self.account_balance):
        self.account_balance -= amount 
        return f"Withdrew: ${self.account_balance}"
    else:
        return "Insufficient funds."
def display_balance(self):
    print (f"Current Balance: ${self.account_balance}")