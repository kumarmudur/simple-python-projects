# banking system app

def menu():
    print("--- Banking System ---")
    print("1. Check Balance\n2. Deposit\n3. Withdraw\n4. Quit")


balance = 0

while True:
    menu()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Balance: ", balance)
    elif choice == 2:
        amount = int(input("Enter the amount to deposit: "))
        balance += amount
    elif choice == 3:
        amount = int(input("Enter the amount to withdraw: "))
        balance -= amount
    elif choice == 4:
        print("Thank you for using ur banking system")
        break
