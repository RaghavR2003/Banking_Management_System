from db_connect import cur

from admin_menu import admin_menu


def admin_login():

    print("\n===== ADMIN LOGIN =====")

    username = input(
        "Username : "
    )

    password = input(
        "Password : "
    )

    cur.execute(
        """
        SELECT *
        FROM admin_login
        WHERE username = :1
        AND password = :2
        """,
        [username, password]
    )

    data = cur.fetchone()

    if data:

        print("\nAdmin Login Successful")

        admin_menu()

    else:

        print(
            "\nInvalid Admin Credentials"
        )