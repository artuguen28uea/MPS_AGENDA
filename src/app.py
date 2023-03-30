from flask import Flask, render_template, request, flash, redirect
from flask_mysqldb import MySQL

app = Flask(__name__, template_folder='templates')
app.secret_key = "149205"

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'mps'
app.config['MYSQL_PASSWORD'] = 'Arabicoffee1006'
app.config['MYSQL_DB'] = 'mydb'

mysql = MySQL(app)

id = 1
status = 0
name = ""
username = ""
email= ""
password = ""

def set_id(idi):
    global id
    id = idi

def set_name(nam):
    global name
    name = nam

def set_status(st):
    global status
    status = st

def set_username(unam):
    global username
    username = unam

def set_email(eml):
    global email
    email = eml

def set_password(psswd):
    global password
    password = psswd

@app.route("/")
def Login():
    return render_template("login_page.html")

@app.route("/registering")
def Registering():
     return render_template("registering_page.html")

@app.route("/back_login")
def Back_lgpage():
     global id
     cursor = mysql.connection.cursor()
     cursor.execute(f"UPDATE agenda_usuario SET usuario_status = %s WHERE usuario_id = %s", (0, id))
     mysql.connection.commit()
     cursor.close()
     return render_template("login_page.html")

@app.route("/user_info")
def User_info():
     return render_template("user_s_informations_page.html")

@app.route("/back_calendar")
def Back_calendar():
     return render_template("calendar_page.html")

@app.route("/verify_login", methods=["GET", "POST"])
def Verify():
   global id
   cursor = mysql.connection.cursor()
   cursor.execute("SELECT * FROM agenda_usuario")

   agenda_usuario = cursor.fetchall()
   
   valid = "False"
   if request.method == "POST":
       for dt in agenda_usuario:
           print(dt)
           if dt[5] == request.form['username'] and dt[4] == request.form['password']:
               set_id(dt[0])
               set_name(dt[1])
               set_email(dt[2])
               set_status(dt[3])
               set_password(dt[4])
               set_username(dt[5])
               valid = "True"
               cursor.execute(f"UPDATE agenda_usuario SET usuario_status = %s WHERE usuario_id = %s", (1, id))
               break
   
   mysql.connection.commit()
   cursor.close()
   return (Initial_page(valid))

@app.route("/initial_page")
def Initial_page(val):
    if val == "True":
        return render_template("calendar_page.html")
    
    flash("uncorrect username or password")
    return redirect("/")
        

@app.route("/add_user", methods=["GET", "POST"])
def Signing():
   user_dt = []
   cursor = mysql.connection.cursor()
  
   if request.method == 'POST':
       user_dt.append(request.form['your_full_name'])
       user_dt.append(request.form['your_email'])
       user_dt.append(0)
       user_dt.append(request.form['your_password'])
       user_dt.append(request.form['your_username'])
       confirmation = request.form['confirm_your_password']
       user_dt = tuple(user_dt)

       if "" not in user_dt and user_dt[3] == confirmation:
            cursor.execute("insert into agenda_usuario(usuario_nome, usuario_email,"
               "usuario_status, usuario_senha, usuario_nome_user) values(%s, %s, %s, %s, %s)", user_dt)
   else:
       flash("uncorrect data insertion")

   mysql.connection.commit()
   cursor.close()

   return render_template("registering_page.html")

@app.route("/update_user", methods=["GET", "POST"])
def Update():
   print(f"O id é {id}")
   user_dt = []
   cursor = mysql.connection.cursor()

   if request.method == 'POST':
       user_dt.append(request.form['full_name'])
       if user_dt[0] != "":
           cursor.execute(f"UPDATE agenda_usuario SET usuario_nome = %s WHERE usuario_id = %s",
    (user_dt[0], id))
           
       user_dt.append(request.form['username'])
       if user_dt[1] != "":
           cursor.execute(f"UPDATE agenda_usuario SET usuario_nome_user = %s WHERE usuario_id = %s",
    (user_dt[1], id))
           
       user_dt.append(request.form['email'])
       if user_dt[2] != "":
           cursor.execute(f"UPDATE agenda_usuario SET usuario_email = %s WHERE usuario_id = %s",
    (user_dt[2], id))
           
       user_dt.append(request.form['password'])
       if user_dt[3] != "":
           cursor.execute(f"UPDATE agenda_usuario SET usuario_senha = %s WHERE usuario_id = %s",
    (user_dt[3], id))
           
       user_dt = tuple(user_dt)

   mysql.connection.commit()

   cursor.execute("SELECT * FROM agenda_usuario")

   agenda_usuario = cursor.fetchall()

   cursor.close()
   return redirect("/user_info", data = agenda_usuario)

@app.route("/delete_user", methods=["POST"])
def Delete():
   cursor = mysql.connection.cursor()
   if request.method == 'POST':
       cursor.execute(f"UPDATE agenda_usuario SET usuario_status = %s WHERE usuario_id = %s", (2, id))

   mysql.connection.commit()
   cursor.close()

   return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)
