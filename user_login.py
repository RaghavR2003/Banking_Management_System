from db_connect import cur

from user_menu import user_menu


def user_login():

    print("\n===== USER LOGIN =====")

    username = input(
        "Username : "
    )

    password = input(
        "Password : "
    )

    cur.execute(
        """
        SELECT account_no
        FROM user_login
        WHERE username = :1
        AND password = :2
        """,
        [username, password]
    )

    data = cur.fetchone()

    if data:

        print("\nLogin Successful")

        user_menu(data[0])

    else:

        print(
            "\nInvalid Username or Password"
        )