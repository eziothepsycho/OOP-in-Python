from bank_account import SavingAccount, CheckingAccount
import random
import string
class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.list_of_accounts = []

    def open_account(self, name, account_type, starting_balance = 5000):
        account_number = ''
        for i in range(6):
            account_number += random.choice(string.ascii_uppercase + string.digits)

        if account_type == "saving":
            new_account = SavingAccount(name, account_number, current_balance=starting_balance)
            self.list_of_accounts.append(new_account)
        elif account_type == "checking":
            new_account = CheckingAccount(name, account_number, current_balance=starting_balance)
            self.list_of_accounts.append(new_account)
        else:
            print(f"Error: Unknown account type '{account_type}'")
        
    def find_account(self, account_number):
        for account in self.list_of_accounts:
            if account.account_number == account_number:
                return account
            else:
                print("Account Not Found!")
    
    def show_all_accounts(self):
        print(f"--- All Accounts in {self.bank_name} ---")
        for i, account in enumerate(self.list_of_accounts, 1):
            account_type = "Savings" if isinstance(account, SavingAccount) else "Checking"
            print(f"{i}. {account.account_name} ({account.account_number}) - {account_type} - ${account.current_balance}")
    
    
