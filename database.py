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

use_db = cursor.execute("USE python_db")

use_db

for py_db in cursor:
  print(py_db, "hello")

# Create a table in the database w/ 2 columns
cursor.execute("CREATE TABLE players (name VARCHAR(255), number INTEGER(10), position VARCHAR(255))")

for py_tbl in cursor:
  print(py_tbl, "umm hey")

# Populating the sql database
sql_ins = "INSERT INTO players (name, number, position) VALUES (%s, %s, %s)"
# Add one
player1 = ("Rodrigo Perez", 6, "Center Midfield")

cursor.execute(sql_ins, player1)

# Add multiple together
playerList = [
  ("Marshall Hendricks", 1, "Goalkeeper"),
  ("Trevor Smiths", 4, "Centerback"),
  ("Wolfgang Stryker", 9, "Forward"),
  ("James Hood", 5, "Rightback"),
  ("Obi Mutumbo", 8, "Holding Midfield"),
  ("Clay Antwort", 7, "Winger"),
  ("Axwell Wellington", 2, "Centerback"),
  ("Trevor Smiths", 4, "Centerback"),
  ("Andrei Prislav", 10, "Attacking Midfield")
]

cursor.executemany(sql_ins, playerList)

# Update the database
sql_update = "UPDATE players SET number = 23 WHERE name = 'James Hood'"

cursor.execute(sql_update)

sql_delete = "DELETE FROM players WHERE name = 'Trevor Smiths'"

cursor.execute(sql_delete)

# Saves the changes to database
db.commit()

# Select a limited amount from the database
cursor.execute("SELECT * FROM players LIMIT 3 OFFSET 3")

select_limited = cursor.fetchall()

for result in select_limited:
  print("first 3", result)

# Select and order the query add DESC for descending order
sql_order = "SELECT * FROM players ORDER BY number DESC"

cursor.execute(sql_order)

order_result = cursor.fetchall()

for result in order_result:
  print("order by num", result)

# Query more specific using WHERE
sql_where = "SELECT * FROM players WHERE position = 'Centerback'"

cursor.execute(sql_where)

where_result = cursor.fetchall()

for result in where_result:
  print("CB", result)

# Query to find all with similarities Ex. below is all that have ll in the middle, ll% would be starts with ll etc.
sql_like = "SELECT * FROM players WHERE name LIKE '%ll%'"

cursor.execute(sql_like)

like_result = cursor.fetchall()

for result in like_result:
  print("like query", result) 

# Get all the data in the table
cursor.execute("SELECT * FROM players")

select_all = cursor.fetchall()

for result in select_all:
  print("player", result)

# Get specific column
cursor.execute("SELECT number FROM players")

select_specific = cursor.fetchone()

for result in select_specific:
  print("player number", result)