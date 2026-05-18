from banking_operation import *


def user_menu(acc):

    while True:

        print("\n==========================")
        print("      USER DASHBOARD")
        print("==========================")

        print("1. Deposit")
        print("2. Withdraw")
        print("3. Transfer")
        print("4. Balance Check")
        print("5. Transaction History")
        print("6. Logout")

        choice = int(
            input("Enter Choice : ")
        )

        if choice == 1:

            deposit(acc)

        elif choice == 2:

            withdraw(acc)

        elif choice == 3:

            transfer(acc)

        elif choice == 4:

            balance_check(acc)

        elif choice == 5:

            transaction_history(acc)

        elif choice == 6:

            print("Logged Out")

            break

        else:

            print("Invalid Choice")