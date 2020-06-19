import mysql.connector


# Connect to MySQL and creating a database
db = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "rootroot",
  database = "python_db"
)

cursor = db.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS python_db")

cursor.execute("SHOW DATABASES")

for py_db in cursor:
  print(py_db)

# Create a table in the database w/ 2 columns
cursor.execute("CREATE TABLE IF NOT EXISTS players (name VARCHAR(255), position INTEGER(10))")

for py_tbl in cursor:
  print(py_tbl)