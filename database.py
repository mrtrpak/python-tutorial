import mysql.connector

config = {
  "user": "root",
  "password": "rootroot",
  "host": "localhost"
}

db = mysql.connector.connect(**config)
cursor = db.cursor()