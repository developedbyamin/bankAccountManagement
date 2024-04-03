from datetime import datetime

class BankAccount:
    def __init__(self, account_number, account_holder_name, account_type, initial_balance=0):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.account_type = account_type
        self.balance = initial_balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append((datetime.now(), 'Deposit', amount))
            print('Deposit successful.')
        else:
            print('Invalid amount for deposit.')

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append((datetime.now(), 'Withdrawal', amount))
            print('Withdrawal successful.')
        else:
            print('Insufficient funds or invalid amount for withdrawal.')

    def get_balance(self):
        return self.balance

    def display_transaction_history(self):
        print(f"Transaction History for Account Number: {self.account_number}")
        print("Date/Time\t\t\tTransaction Type\t\tAmount")
        for transaction in self.transaction_history:
            print(f"{transaction[0]}\t{transaction[1]}\t\t${transaction[2]}")

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder_name, initial_balance=0, interest_rate=0.01):
        super().__init__(account_number, account_holder_name, 'Savings', initial_balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest_amount = self.balance * self.interest_rate
        self.balance += interest_amount
        self.transaction_history.append((datetime.now(), 'Interest', interest_amount))
        print('Interest added successfully.')

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, account_holder_name, account_type, initial_balance=0):
        if account_number not in self.accounts:
            if account_type == 'Savings':
                self.accounts[account_number] = SavingsAccount(account_number, account_holder_name, initial_balance)
            else:
                self.accounts[account_number] = BankAccount(account_number, account_holder_name, account_type, initial_balance)
            print('Account created successfully.')
        else:
            print('Account number already exists.')

    def close_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            print('Account closed successfully.')
        else:
            print('Account does not exist.')

    def transfer_funds(bank):
        from_account_number = input("Enter account number to transfer from: ")
        to_account_number = input("Enter account number to transfer to: ")
        
        if from_account_number in bank.accounts and to_account_number in bank.accounts:
            amount = float(input("Enter transfer amount: "))
            bank.transfer_funds(from_account_number, to_account_number, amount)
        else:
            print("One or both accounts not found.")


    def display_account_balance(self, account_number):
        if account_number in self.accounts:
            print(f"Balance for Account Number {account_number}: ${self.accounts[account_number].get_balance()}")
        else:
            print('Account does not exist.')

    def display_account_transaction_history(self, account_number):
        if account_number in self.accounts:
            self.accounts[account_number].display_transaction_history()
        else:
            print('Account does not exist.')


def print_menu():
    print("\nWelcome to the Bank Account Management System!")
    print("1. Create New Account")
    print("2. Deposit Funds")
    print("3. Withdraw Funds")
    print("4. Transfer Funds")
    print("5. Close Account")
    print("6. Check Account Balance")
    print("7. View Transaction History")
    print("8. Exit")

def create_account(bank):
    account_number = input("Enter account number: ")
    account_holder_name = input("Enter account holder name: ")
    account_type = input("Enter account type (e.g., Savings, Checking): ")
    initial_balance = float(input("Enter initial balance: "))
    bank.create_account(account_number, account_holder_name, account_type, initial_balance)

def deposit_funds(bank):
    account_number = input("Enter account number: ")
    amount = float(input("Enter deposit amount: "))
    bank.accounts[account_number].deposit(amount)

def withdraw_funds(bank):
    account_number = input("Enter account number: ")
    if account_number in bank.accounts:
        amount = float(input("Enter withdrawal amount: "))
        bank.accounts[account_number].withdraw(amount)
    else:
        print("Account not found.")


def transfer_funds(bank):
    from_account_number = input("Enter account number to transfer from: ")
    to_account_number = input("Enter account number to transfer to: ")
    amount = float(input("Enter transfer amount: "))
    bank.transfer_funds(from_account_number, to_account_number, amount)

def close_account(bank):
    account_number = input("Enter account number to close: ")
    bank.close_account(account_number)

def check_balance(bank):
    account_number = input("Enter account number: ")
    bank.display_account_balance(account_number)

def view_transaction_history(bank):
    account_number = input("Enter account number: ")
    bank.display_account_transaction_history(account_number)

if __name__ == "__main__":
    bank = Bank()

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            create_account(bank)
        elif choice == '2':
            deposit_funds(bank)
        elif choice == '3':
            withdraw_funds(bank)
        elif choice == '4':
            transfer_funds(bank)
        elif choice == '5':
            close_account(bank)
        elif choice == '6':
            check_balance(bank)
        elif choice == '7':
            view_transaction_history(bank)
        elif choice == '8':
            print("Thank you for using the Bank Account Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
