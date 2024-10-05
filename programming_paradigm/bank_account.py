class BankAccount:
    def __init__(self, account_balance=0):
        self.balance = account_balance
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        can_withdraw = 0 < amount <= self.balance
        while True:
            if can_withdraw:
                self.balance -= amount
            else:
                print("Insufficient Funds")
                break
    def display_balance(self):
        print(f'Current Balance: ${self.balance}')
        


        
    

