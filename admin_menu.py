from db_connect import cur


def admin_menu():

    while True:

        print("\n==========================")
        print("       ADMIN PANEL")
        print("==========================")

        print("1. View Customers")
        print("2. View Accounts")
        print("3. View Transactions")
        print("4. Logout")

        choice = int(
            input("Enter Choice : ")
        )

        if choice == 1:

            cur.execute(
                "SELECT * FROM customers"
            )

            rows = cur.fetchall()

            for row in rows:

                print(row)

        elif choice == 2:

            cur.execute(
                "SELECT * FROM accounts"
            )

            rows = cur.fetchall()

            for row in rows:

                print(row)

        elif choice == 3:

            cur.execute(
                "SELECT * FROM transactions"
            )

            rows = cur.fetchall()

            for row in rows:

                print(row)

        elif choice == 4:

            print("Admin Logged Out")

            break

        else:

            print("Invalid Choice")