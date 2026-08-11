"""
Program Name : Bank Account 
Author       : Neeraj Kaushik

Description:
This module contains the BankAccount class which manages
deposit, withdrawal, balance inquiry, money transfer,
and transaction history using Object-Oriented Programming.

"""

# Implementation:

class BankAccount:

    def __init__(self, account_no, holder_name, pin):
        self.account_no = account_no
        self.holder_name = holder_name
        self.__balance = 0          # Initial balance set by bank
        self.__pin = pin
        self.transactions = []

    # ---------------- PIN Verification ---------------- #

    def verify_pin(self, pin):
        return self.__pin == pin

    # ---------------- Deposit ---------------- #

    def deposit(self, amount):

        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return

        self.__balance += amount

        self.transactions.append(
            f"Deposited ₹{amount}"
        )

        print(f"₹{amount} deposited successfully.")

    # ---------------- Withdraw ---------------- #

    def withdraw(self, amount, pin):

        if not self.verify_pin(pin):
            print("Incorrect PIN.")
            return

        if amount <= 0:
            print("Invalid Amount.")
            return

        if amount > self.__balance:
            print("Insufficient Balance.")
            return

        self.__balance -= amount

        self.transactions.append(
            f"Withdrawn ₹{amount}"
        )

        print(f"₹{amount} withdrawn successfully.")

    # ---------------- Transfer ---------------- #

    def transfer(self, receiver, amount, pin):

        if not self.verify_pin(pin):
            print("Incorrect PIN.")
            return

        if amount <= 0:
            print("Invalid Amount.")
            return

        if amount > self.__balance:
            print("Insufficient Balance.")
            return

        self.__balance -= amount
        receiver.__balance += amount

        self.transactions.append(
            f"Transferred ₹{amount} to {receiver.holder_name}"
        )

        receiver.transactions.append(
            f"Received ₹{amount} from {self.holder_name}"
        )

        print("Transfer Successful.")

    # ---------------- Balance ---------------- #

    def show_balance(self, pin):

        if self.verify_pin(pin):
            print(f"Current Balance : ₹{self.__balance}")
        else:
            print("Incorrect PIN.")

    # ---------------- Account Details ---------------- #

    def account_details(self):

        print("\n----------- ACCOUNT DETAILS -----------")
        print("Account Number :", self.account_no)
        print("Account Holder :", self.holder_name)
        print("---------------------------------------")

    # ---------------- Transaction History ---------------- #

    def transaction_history(self):

        print("\n------- Transaction History -------")

        if not self.transactions:
            print("No Transactions Yet.")

        else:

            for transaction in self.transactions:
                print(transaction)

    # ---------------- Getter ---------------- #

    def get_balance(self):
        return self.__balance


class Bank:

    def __init__(self):

        # Dictionary to store accounts
        self.accounts = {}

        # Starting Account Number
        self.next_account_no = 1001

    # ---------------- Create Account ---------------- #

    def create_account(self):

        holder_name = input("Enter Account Holder Name : ")

        pin = int(input("Set 4-digit PIN : "))

        account = BankAccount(
            self.next_account_no,
            holder_name,
            pin
        )

        self.accounts[self.next_account_no] = account

        print("\n--------------------------------")
        print("Account Created Successfully")
        print(f"Account Number : {self.next_account_no}")
        print("Initial Balance : ₹0")
        print("--------------------------------")

        self.next_account_no += 1

    # ---------------- Find Account ---------------- #

    def get_account(self, account_no):

        return self.accounts.get(account_no)

    # ---------------- Deposit ---------------- #

    def deposit_money(self):

        account_no = int(input("Enter Account Number : "))

        account = self.get_account(account_no)

        if account:

            amount = float(input("Enter Amount : "))

            account.deposit(amount)

        else:

            print("Account Not Found.")

    # ---------------- Withdraw ---------------- #

    def withdraw_money(self):

        account_no = int(input("Enter Account Number : "))

        account = self.get_account(account_no)

        if account:

            pin = int(input("Enter PIN : "))

            amount = float(input("Enter Amount : "))

            account.withdraw(amount, pin)

        else:

            print("Account Not Found.")

    # ---------------- Balance ---------------- #

    def check_balance(self):

        account_no = int(input("Enter Account Number : "))

        account = self.get_account(account_no)

        if account:

            pin = int(input("Enter PIN : "))

            account.show_balance(pin)

        else:

            print("Account Not Found.")

    # ---------------- Account Details ---------------- #

    def account_details(self):

        account_no = int(input("Enter Account Number : "))

        account = self.get_account(account_no)

        if account:

            account.account_details()

        else:

            print("Account Not Found.")

    # ---------------- Transaction History ---------------- #

    def transaction_history(self):

        account_no = int(input("Enter Account Number : "))

        account = self.get_account(account_no)

        if account:

            account.transaction_history()

        else:

            print("Account Not Found.")

    # ---------------- Transfer Money ---------------- #

    def transfer_money(self):

        sender_account = int(input("Enter Sender Account Number : "))

        receiver_account = int(input("Enter Receiver Account Number : "))

        sender = self.get_account(sender_account)

        receiver = self.get_account(receiver_account)

        if sender is None:

            print("Sender Account Not Found.")
            return

        if receiver is None:

            print("Receiver Account Not Found.")
            return

        pin = int(input("Enter PIN : "))

        amount = float(input("Enter Amount : "))

        sender.transfer(receiver, amount, pin)

        # ---------------- Main Program ---------------- #

bank = Bank()

while True:

    print("\n==========================================")
    print("      BANK MANAGEMENT SYSTEM")
    print("==========================================")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transfer Money")
    print("5. Check Balance")
    print("6. Account Details")
    print("7. Transaction History")
    print("8. Exit")
    print("==========================================")

    choice = int(input("Enter Your Choice : "))

    if choice == 1:

        bank.create_account()

    elif choice == 2:

        bank.deposit_money()

    elif choice == 3:

        bank.withdraw_money()

    elif choice == 4:

        bank.transfer_money()

    elif choice == 5:

        bank.check_balance()

    elif choice == 6:

        bank.account_details()

    elif choice == 7:

        bank.transaction_history()

    elif choice == 8:

        print("\nThank You For Using Bank Management System.")
        break

    else:

        print("Invalid Choice. Please Try Again.")