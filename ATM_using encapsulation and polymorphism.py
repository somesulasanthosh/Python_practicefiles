class ATM:

    def __init__(self, name, balance=10000, pin="4077"):
        self.name = name            # Public
        self._balance = balance     # Protected
        self.__pin = pin            # Private
        self.transactions = []

    def check_pin(self):
        entered_pin = input("Enter ATM PIN: ")

        if entered_pin == self.__pin:
            return True

        print("Incorrect PIN")
        return False

    def credit(self):
        amount = float(input("Enter amount to credit: ₹"))

        if amount > 0:
            self._balance += amount
            self.transactions.append(f"Credited ₹{amount}")
            print(f"₹{amount} credited successfully")
        else:
            print("Invalid amount")

    def debit(self):
        amount = float(input("Enter amount to debit: ₹"))

        if amount <= 0:
            print("Invalid amount")

        elif amount > self._balance:
            print("Insufficient balance")

        else:
            self._balance -= amount
            self.transactions.append(f"Debited ₹{amount}")
            print(f"₹{amount} debited successfully")

    def show_balance(self):
        print(f"Available Balance: ₹{self._balance}")

    def mini_statement(self):

        print("\n------ MINI STATEMENT ------")

        if len(self.transactions) == 0:
            print("No transactions found")
        else:
            for transaction in self.transactions:
                print(transaction)

        print(f"Current Balance: ₹{self._balance}")

    def change_pin(self):

        old_pin = input("Enter old PIN: ")

        if old_pin == self.__pin:

            new_pin = input("Enter new PIN: ")
            confirm_pin = input("Confirm new PIN: ")

            if new_pin == confirm_pin:
                self.__pin = new_pin
                print("PIN changed successfully")
            else:
                print("PIN mismatch")

        else:
            print("Wrong old PIN")



class SavingsATM(ATM):

    def credit(self):
        print("Savings Account Credit")
        super().credit()

    def debit(self):
        print("Savings Account Debit")
        super().debit()


atm = SavingsATM("Santhosh")

while True:

    print("\n===== ATM MENU =====")
    print("1. Credit")
    print("2. Debit")
    print("3. Balance")
    print("4. Mini Statement")
    print("5. Change PIN")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        if atm.check_pin():
            atm.credit()

    elif choice == '2':
        if atm.check_pin():
            atm.debit()

    elif choice == '3':
        if atm.check_pin():
            atm.show_balance()

    elif choice == '4':
        if atm.check_pin():
            atm.mini_statement()

    elif choice == '5':
        if atm.check_pin():
            atm.change_pin()

    elif choice == '6':
        print("Thank you for using ATM")
        break

    else:
        print("Invalid choice")