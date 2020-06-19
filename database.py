import mysql.connector;


# Connect to MySQL and creating a database
db = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "rootroot",
  database = "python_db"
)

cursor = db.cursor()

cursor.execute("DROP DATABASE IF EXISTS python_db")

cursor.execute("CREATE DATABASE IF NOT EXISTS python_db")

cursor.execute("USE python_db")

for py_db in cursor:
  print(py_db)

# Create a table in the database w/ 2 columns
cursor.execute("CREATE TABLE players (name VARCHAR(255), number INTEGER(10), position VARCHAR(255))")

for py_tbl in cursor:
  print(py_tbl)

# Populating the sql database
sqlFormula = "INSERT INTO players (name, number, position) VALUES (%s, %s, %s)"

player1 = ("Marshall Hendricks", 1, "Goalkeeper")
player2 = ("Trevor Smiths", 4, "Centerback")
player3 = ("Wolfgang Stryker", 9, "Centerforward")

cursor.execute(sqlFormula, player1)
cursor.execute(sqlFormula, player2)
cursor.execute(sqlFormula, player3)

# Saves the change to database
db.commit()