import oracledb

# Enable Thick Mode
oracledb.init_oracle_client(
    lib_dir=r"C:\oracle\instantclient_23_0"
)

# Connect to Oracle XE
conn = oracledb.connect(
    user="bankdb",
    password="bank123",
    dsn="localhost/xe"
)

cur = conn.cursor()


