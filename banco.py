import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  port="3307",
  user="root",
  password="Art_uguen2805!",
  database="mydb"
)

mycursor = mydb.cursor()

# sql = "INSERT INTO agenda_usuario (usuario_id, usuario_nome, usuario_email, usuario_status, usuario_senha, usuario_nome_user) VALUES (%s, %s, %s, %s, %s, %s)"
# val = (2, "Alexandre", "alexandreuguen20@gmail.com", 0, "12345", "alexandreuguen")
# mycursor.execute(sql, val)

# mydb.commit()

mycursor.execute("select * from agenda_usuario")

myresult = mycursor.fetchall()
for x in myresult:
  print(x)