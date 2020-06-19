import mysql.connector

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
sql = "INSERT INTO players (name, number, position) VALUES (%s, %s, %s)"
# Add one
player1 = ("Rodrigo Perez", 8, "Center Midfield")

cursor.execute(sql, player1)

# Add multiple together
playerList = [
  ("Marshall Hendricks", 1, "Goalkeeper"),
  ("Trevor Smiths", 4, "Centerback"),
  ("Wolfgang Stryker", 9, "Forward"),
  ("James Hood", 5, "Rightback"),
  ("Obi Mutumbo", 8, "Holding Midfield"),
  ("Clay Antwort", 7, "Winger"),
  ("Axwell Wellington", 2, "Centerback"),
  ("Andrei Prislav", 10, "Attacking Midfield")
]

cursor.executemany(sql, playerList)

# Saves the change to database
db.commit()

# Get all the data in the table
cursor.execute("SELECT * FROM players")

result = cursor.fetchall()

for row in result:
  print(row)

# Get specific column
cursor.execute("SELECT number FROM players")

result2 = cursor.fetchone()

for row in result2:
  print(row)


