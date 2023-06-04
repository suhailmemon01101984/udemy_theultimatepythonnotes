class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        self.transactions = [f'Initial balance: {balance}']

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f'Deposit: {amount}')

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(f'Withdrawal: {amount}')
        else:
            print('Insufficient funds.')

    def get_balance(self):
        return self.balance

