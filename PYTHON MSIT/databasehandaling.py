import mysql.connector
mydb =mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

abc = mydb.cursor()

abc.execute("CREATE DATABASE msit")
print("Database Created Successfully")