from db_connect import cur

def view_balance():

    print("\n===== VIEW BALANCE =====")

    acc_no = int(
        input("Enter Account Number : ")
    )

    balance = cur.var(float)

    cur.callproc(
        "view_balance",
        [acc_no, balance]
    )

    if balance.getvalue() == -1:

        print("\nAccount Not Found")

    else:

        print(
            "\nCurrent Balance =",
            balance.getvalue()
        )