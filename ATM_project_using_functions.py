balance = 100000
pin = "1234"
transactions = []



def check_pin():
    entered_pin = input("Enter ATM PIN: ")

    if entered_pin == pin:
        return True
    else:
        print("Incorrect PIN")
        return False


def credit():
    global balance

    amount = float(input("Enter amount to credit: ₹"))

    if amount <= 0:
        print("Invalid amount")
    else:
        balance += amount
        transactions.append(f"Credited ₹{amount}")
        print(f"₹{amount} credited successfully")



def debit():
    global balance

    amount = float(input("Enter amount to debit: ₹"))

    if amount <= 0:
        print("Invalid amount")

    elif amount > balance:
        print("Insufficient balance")

    else:
        balance -= amount
        transactions.append(f"Debited ₹{amount}")
        print(f"₹{amount} debited successfully")



def show_balance():
    print(f"Available Balance: ₹{balance}")



def mini_statement():

    print("\n------ MINI STATEMENT ------")

    if len(transactions) == 0:
        print("No transactions found")

    else:
        for i in transactions:
            print(i)

    print(f"Current Balance: ₹{balance}")


def change_pin():
    global pin

    old_pin = input("Enter old PIN: ")

    if old_pin == pin:

        new_pin = input("Enter new PIN: ")
        confirm_pin = input("Confirm new PIN: ")

        if new_pin == confirm_pin:
            pin = new_pin
            print("PIN changed successfully")

        else:
            print("PIN mismatch")

    else:
        print("Wrong old PIN")


# Main ATM Menu
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
        if check_pin():
            credit()

    elif choice == '2':
        if check_pin():
            debit()

    elif choice == '3':
        if check_pin():
            show_balance()

    elif choice == '4':
        if check_pin():
            mini_statement()

    elif choice == '5':
        if check_pin():
            change_pin()

    elif choice == '6':
        print("Thank you for using ATM")
        break

    else:
        print("Invalid choice")