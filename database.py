import mysql.connector

db = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "rootroot"
)

cursor = db.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS python_db")