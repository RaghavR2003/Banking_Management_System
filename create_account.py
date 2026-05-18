from db_connect import cur


def create_account():

    print("\n===== CREATE ACCOUNT =====")

    name = input("Enter Name : ")

    phone = input("Enter Phone : ")

    email = input("Enter Email : ")

    address = input("Enter Address : ")

    acc_type = input("Account Type : ")

    balance = float(
        input("Initial Balance : ")
    )

    username = input(
        "Create Username : "
    )

    password = input(
        "Create Password : "
    )

    account_no = cur.var(int)

    cur.callproc(
        "create_account",
        [
            name,
            phone,
            email,
            address,
            acc_type,
            balance,
            username,
            password,
            account_no
        ]
    )

    print("\n================================")
    print("Account Created Successfully")
    print("Your Account Number is :",
          account_no.getvalue())
    print("================================")