import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234"
)

cursor = conn.cursor()
cursor.execute("CREATE DATABASE Regexl4")

print("Database created successfully!")
