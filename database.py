import mysql.connector

db = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "rootroot"
)

print(db)

cursor = db.cursor()