#Example 1: Bank Account

'''
This example demonstrates how to create a BankAccount 
class using object-oriented programming principles in Python.
'''

class BankAccount:
    """
    A class representing a bank account.
    """
    
    def __init__(self, account_number, balance=0):
        """
        Initializes a new bank account object.
        """
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        """
        Deposits the given amount into the account.
        """
        self.balance += amount
    
    def withdraw(self, amount):
        """
        Withdraws the given amount from the account.
        """
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")
    
    def get_balance(self):
        """
        Returns the current balance of the account.
        """
        return self.balance
    
    def __str__(self):
        """
        Returns a string representation of the account.
        """
        return f"Account number: {self.account_number}, Balance: {self.balance}"


'''
In this example, we define a BankAccount class that has four methods:
__init__, deposit, withdraw, and get_balance. 
The __init__ method is a constructor that initializes a 
new BankAccount object with an account number and an optional initial balance. 
The deposit and withdraw methods modify the balance of the account by adding or 
subtracting the given amount, respectively. 
The get_balance method returns the current balance of the account. 
The __str__ method returns a string representation of the account, 
which is used when the object is printed.
'''

# Create a new bank account
account = BankAccount("123456789")

# Deposit some money
account.deposit(1000)

# Withdraw some money
account.withdraw(500)

# Print the current balance
print(account.get_balance())

# Print the account details
print(account)


'''
we create a new BankAccount object with an account number of "123456789". 
We deposit 1000 into the account and then withdraw 500, leaving a balance of 500. 
We print the current balance using the get_balance method, 
which returns the balance as a string. Finally, 
we print the account details using the __str__ method, 
which returns a string representation of the account

'''