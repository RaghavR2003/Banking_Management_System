from db_connect import cur


def deposit(acc):

    amount = float(
        input("Enter Amount : ")
    )

    cur.callproc(
        "deposit_money",
        [acc, amount]
    )

    print("Money Deposited Successfully")


def withdraw(acc):

    amount = float(
        input("Enter Amount : ")
    )

    cur.callproc(
        "withdraw_money",
        [acc, amount]
    )

    print("Money Withdrawn Successfully")


def transfer(acc):

    receiver = int(
        input(
            "Receiver Account Number : "
        )
    )

    amount = float(
        input("Enter Amount : ")
    )

    cur.callproc(
        "transfer_money",
        [acc, receiver, amount]
    )

    print("Transfer Successful")


def balance_check(acc):

    cur.execute(
        """
        SELECT balance
        FROM accounts
        WHERE account_no = :1
        """,
        [acc]
    )

    data = cur.fetchone()

    print(
        "\nCurrent Balance =",
        data[0]
    )


def transaction_history(acc):

    cur.execute(
        """
        SELECT transaction_type,
               amount,
               transaction_date
        FROM transactions
        WHERE account_no = :1
        ORDER BY transaction_date DESC
        """,
        [acc]
    )

    rows = cur.fetchall()

    print(
        "\n===== TRANSACTION HISTORY ====="
    )

    for row in rows:

        print(
            row[0],
            "|",
            row[1],
            "|",
            row[2]
        )