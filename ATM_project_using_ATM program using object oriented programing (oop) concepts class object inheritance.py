class ATM:

    def __init__(self, bank, branch, location, balance=10000, pin="1234"):
        self.bank = bank
        self.branch = branch
        self.location = location
        self.balance = balance
        self.pin = pin
        self.transactions = []


        print("\n===== ATM DETAILS =====")
        print("Bank Name :", self.bank)
        print("Branch    :", self.branch)
        print("Location  :", self.location)
        print("Balance   :", self.balance)

    def check_pin(self):
        entered_pin = input("Enter ATM PIN: ")

        if entered_pin == self.pin:
            return True
        else:
            print("Incorrect PIN")
            return False

    def credit(self):

        amount = float(input("Enter amount to credit: ₹"))

        if amount <= 0:
            print("Invalid amount")

        else:
            self.balance += amount
            self.transactions.append(f"Credited ₹{amount}")
            print(f"₹{amount} credited successfully")

    def debit(self):

        amount = float(input("Enter amount to debit: ₹"))

        if amount <= 0:
            print("Invalid amount")

        elif amount > self.balance:
            print("Insufficient balance")

        else:
            self.balance -= amount
            self.transactions.append(f"Debited ₹{amount}")
            print(f"₹{amount} debited successfully")

    def show_balance(self):
        print(f"Available Balance: ₹{self.balance}")

    def mini_statement(self):

        print("\n------ MINI STATEMENT ------")

        if len(self.transactions) == 0:
            print("No transactions found")

        else:
            for i in self.transactions:
                print(i)

        print(f"Current Balance: ₹{self.balance}")

    def change_pin(self):

        old_pin = input("Enter old PIN: ")

        if old_pin == self.pin:

            new_pin = input("Enter new PIN: ")
            confirm_pin = input("Confirm new PIN: ")

            if new_pin == confirm_pin:
                self.pin = new_pin
                print("PIN changed successfully")

            else:
                print("PIN mismatch")

        else:
            print("Wrong old PIN")



HDFC = ATM("HDFC", "Nandyal", "opp raj theater Nandyal,kurnool dist")



while True:

    print("\n===== ATM MENU =====")
    print("1. Credit")
    print("2. Debit")
    print("3. Balance")
    print("4. Mini Statement")
    print("5. Change PIN")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        if HDFC.check_pin():
            HDFC.credit()

    elif choice == "2":
        if HDFC.check_pin():
            HDFC.debit()

    elif choice == "3":
        if HDFC.check_pin():
            HDFC.show_balance()

    elif choice == "4":
        if HDFC.check_pin():
            HDFC.mini_statement()

    elif choice == "5":
        if HDFC.check_pin():
            HDFC.change_pin()

    elif choice == "6":
        print("Thank you for using ATM")
        break

    else:
        print("Invalid choice")