#Class account
class Account:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Withdrawal amount must be positive and less than or equal to the balance.")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account Number: {self.account_number}, Account Holder: {self.account_holder}, Balance: {self.balance}"
    
    
Account1=Account(account_number="123456", account_holder="Mayank Joshi", balance=1000)
Account1.deposit(500) 
Account1.withdraw(200)
print(Account1.get_balance())
Account1.withdraw(1500)
Account1.withdraw(100)
account2=Account(account_number="654321", account_holder="John Doe", balance=500)
account2.deposit(300)
print(account2.get_balance())
print(Account1)
print(account2)
print(getattr(Account1, 'account_holder'))