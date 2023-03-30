import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  port="3307",
  user="root",
  password="Art_uguen2805!",
  database="mydb"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)