from datetime import datetime
class BankAccount:
    def __init__(self, account_name, account_number, current_balance = 5000):
        self.account_name = account_name
        self.account_number = account_number
        self.current_balance = current_balance
        self.transactions = []
    
    def deposit(self, amount):
        if amount > 0:
            self.current_balance += amount
            print(f"You deposit {amount}. Balance: {self.current_balance}")
            self.add_transaction(datetime.now(), amount, 'deposit')
        else:
            print(f"Insufficient Balance: {self.current_balance}")
    
    def withdraw(self, amount):
        if self.current_balance > amount:
            self.current_balance -= amount
            print(f"You withdraw {amount}. Balance: {self.current_balance}")
            self.add_transaction(datetime.now(), amount, 'withdrawal')
        else:
            print(f"Error. Insufficient Balance: {self.current_balance}")
    
    def check_balance(self):
        print(f"Your Balance is: {self.current_balance}")
    
    def add_transaction(self, current_time, amount, transaction_type):
        current_time = current_time.strftime("%Y-%m-%d")
        transaction = {
            'date': current_time,
            'type': transaction_type, 
            'amount': amount,
            'balance': self.current_balance
        }
        self.transactions.append(transaction)
        print(f"\nDate: {current_time}\nType: {transaction_type}\nAmount: {amount}\nBalance After: {self.current_balance}")

class SavingAccount(BankAccount):
    def __init__(self, account_name, account_number, current_balance=5000, interest_rate = 0.05):
        super().__init__(account_name, account_number, current_balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest_amount = self.current_balance * self.interest_rate
        self.current_balance += interest_amount
        print(f"Interest added: ${interest_amount:.2f}. New Balance: ${self.current_balance:.2f}")

class CheckingAccount(BankAccount):
    def __init__(self, account_name, account_number, overdraft_limit = 100, current_balance=5000):
        super().__init__(account_name, account_number, current_balance)
        self.overdraft_limit = overdraft_limit

    
    def withdraw(self, amount):
        if (self.current_balance - amount) >= -self.overdraft_limit:
            self.current_balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.current_balance}")
            self.add_transaction(datetime.now(), amount, 'withdrawal')
        else:
            print(f"Error! Overdraft limit exceeded. Available: ${self.current_balance + self.overdraft_limit}")