class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance>amount:
            self.balance -= amount
    
    def get_balance(self):
        return self.balance
    
account = BankAccount(100)
account.withdraw(40)
print(account.get_balance())
account.deposit(100)
print(account.get_balance())