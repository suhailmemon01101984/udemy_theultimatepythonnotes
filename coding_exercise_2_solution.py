class BankAccount:
    def __init__(self,account_number,balance):
        self.account_number=account_number
        self.balance=balance
        self.transactions=[]
    def deposit(self,amount):
        self.balance=self.balance+amount
        self.transactions.append(f"Deposited amount: {amount}. New Balance: {self.balance}")
    def withdraw(self,amount):
        if(self.balance-amount >= 0):
            self.balance=self.balance-amount
            self.transactions.append(f"Withdrew amount: {amount}. New Balance: {self.balance}")
        else:
            print("Insufficient funds")
    def get_balance(self):
        return f"Current Balance: {self.balance}"
    def get_transactions(self):
        return f"Current Transaction List: {self.transactions}"


account1=BankAccount(123456,100)
print(account1.get_balance())
print(account1.get_transactions())
account1.deposit(200)
print(account1.get_balance())
print(account1.get_transactions())
account1.deposit(100)
print(account1.get_balance())
print(account1.get_transactions())
account1.deposit(250)
print(account1.get_balance())
print(account1.get_transactions())
account1.withdraw(100)
print(account1.get_balance())
print(account1.get_transactions())
account1.withdraw(550)
print(account1.get_balance())
print(account1.get_transactions())