from bank_account import BankAccount, SavingAccount, CheckingAccount
from bank import Bank

class BankApp:
    def __init__(self):
        self.bank = None
        self.running = True
    
    def show_menu(self):
        print("\n=== BANK MANAGEMENT SYSTEM ===")
        print("1. Create Bank")
        print("2. Open New Account")
        print("3. Find Account")
        print("4. Show All Accounts")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        return choice

    def run(self):
        while self.running:
            choice = self.show_menu()
            if choice == "1":
                self.create_bank()
            elif choice == "2":
                self.open_account()
            elif choice == "3":
                self.find_account()
            elif choice == "4":
                self.show_all_accounts()
            elif choice == "5":
                self.running == False   
            else:
                print("Wrong input!")
    
    def create_bank(self):
        name = input("Enter your bank name: ")
        self.bank = Bank(name)
        print(f"You created {self.bank.bank_name}! successfully.")
    
    def open_account(self):
        if self.bank is None:
            print("Please create your bank first.")
            return

        name = input("Enter your name: ")
        balance_input = input("Enter starting balance (or press Enter for default 5000):")
        if balance_input == "":
            balance = 5000
        else:
            balance = int(balance_input)
        
        account_type = input("Enter you account type(Saving or Checking):")
        if account_type.lower() != "saving" and account_type.lower() != "checking":
            print("Invalid Input.")
        
        else:
            self.bank.open_account(name, account_type, balance)
            print("Account created successfully!")
        
    def find_account(self):
        if self.bank is None:
            print("Please create your bank first.")
            return
        
        account_number = input("Enter the account number: ")
        found_account = self.bank.find_account(account_number)

        if found_account:
            print("\nAccount found!")
            print(f"Name: {found_account.account_name}")
            print(f"Account number: {found_account.account_number}")
            if isinstance(found_account, SavingAccount):
                account_type = "Saving"
            else:
                account_type = "Checking"
            print(f"Account Type: {account_type}")
            print(f"Balance: {found_account.current_balance}")
        else:
            print("Account not found.")
    
    def show_all_accounts(self):
        if self.bank is None:
            print("Please create your bank first.")
            return
        if len(self.bank.list_of_accounts) == 0:
            print("No accounts created.")
        else:
            self.bank.show_all_accounts()
        
if __name__ == "__main__":
    bankapp = BankApp()
    bankapp.run()

