from create_account import create_account
from user_login import user_login
from admin_login import admin_login
from view_balance import view_balance

while True:

    print("\n===================================")
    print("     XYZ INTERNATIONAL BANK")
    print("===================================")

    print("1. Create Account")
    print("2. User Login")
    print("3. Admin Login")
    print("4. View Balance")
    print("5. Exit")

    choice = int(input("Enter Choice : "))

    if choice == 1:

        create_account()

    elif choice == 2:

        user_login()

    elif choice == 3:

        admin_login()

    elif choice == 4:

        view_balance()

    elif choice == 5:

        print("Thank You")
        break

    else:

        print("Invalid Choice")