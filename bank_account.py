# Defining a class to represent a bank account
class Account:
    # For initializing account details
    def __init__(self, account_number, account_holder, account_balance=0.0):
        self.account_number = account_number  # Account number
        self.account_holder = account_holder  # Name of the person who owns the account
        self.account_balance = account_balance  # Current balance 

    # Allows the user to deposit money into the account
    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount  # Add amount to balance
            print(f"{amount} has been deposited to {self.account_holder}'s account.")
        else:
            print("Deposit amount must be greater than zero.")  # Guard against negative or zero deposits

    # Allows the user to withdraw money from the account
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")  # Error if user tries to withdraw while account has no money
        elif amount > self.account_balance:
            print(f"Insufficient balance for {self.account_holder}.")  # Error if user tries to withdraw while account has less money
        else:
            self.account_balance -= amount  # Deducts the amount from the remaining balance
            print(f"{amount} has been withdrawn from {self.account_holder}'s account.")

    # Allows user to check the current balance
    def check_balance(self):
        return self.account_balance

print("*"*50)
print("=== Welcome to the Faida Accounts ===")
# Ask for the users account number and ensures the it is in digits only
while True:
    account_number = input("Enter account number in digits: ")
    if account_number.isdigit():
        break
    else:
        print("Invalid account number. Please enter digits only.")
# Ask for the account holder's name and ensures that it is in letters only
while True:
    account_holder = input("Enter account holder's name: ")
    # Remove extra spaces and normalize spacing
    normalized_name = " ".join(account_holder.strip().split())
    if normalized_name.replace(" ", "").isalpha():
        account_holder = normalized_name
        break
    else:
        print("Invalid name. Please use letters only.")
print("*"*50)

# Creating the account with an optional initial deposit 
try:
    initial_balance = float(input("Enter initial balance: "))
except ValueError:
    print("Invalid input! Setting balance to 0")
    initial_balance = 0.0

my_account = Account(account_number, account_holder, initial_balance)

# While loop for the menu
while True:
    # Show the options for the menu
    print("\nWhat would you like to do?")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    # To obtain the user input
    user_input = input("Enter your choice (1-4): ")

    if user_input == "1":
        # For depositing money
        try:
            amount = float(input("Enter amount to deposit: "))
            my_account.deposit(amount)
        except ValueError:
            print("Invalid amount!")
    elif user_input == "2":
        # For withdrawing money
        try:
            amount = float(input("Enter amount to withdraw: "))
            my_account.withdraw(amount)
        except ValueError:
            print("Invalid amount!")
    elif user_input == "3":
        # Checking the current balance
        print(f"Current Balance: {my_account.check_balance()}")
    elif user_input == "4":
        # Exiting the loop
        print("Exiting!")
        break
    # Checks if the user inputs an invalid choice
    else:
        print("Invalid choice. Please select a valid option.")