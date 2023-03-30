from flask import Flask, redirect, render_template, g, request
from src.models import Validation
from get_ip import get_ip
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  port="3307",
  user="root",
  password="Art_uguen2805!",
  database="mydb"
)

id = 0


app = Flask(__name__)
app.secret_key = "dosfjdsofjoskjeicds_Sd"

# app.register_blueprint(login)
# app.register_blueprint(cadastro)

@app.route("/", methods=["GET"])
def login():
    return render_template("login.html")

@app.route("/", methods=["POST"])
def submit_login():
    forms = request.form
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM agenda_usuario")
    myresult = mycursor.fetchall()
    for x in myresult:
        if (x[2] == forms['uemail']) and (x[4] == forms['pwd']) and (x[3] == 0):
            global id
            id = x[0]
            mycursor = mydb.cursor()
            sql = f"UPDATE agenda_usuario SET usuario_status = 1 WHERE usuario_id = {id}"
            mycursor.execute(sql)
            mydb.commit()
            return render_template("home.html")
        
    return render_template("login.html")


@app.route("/cadastro", methods=["GET"])
def cadastro():
    return render_template("cadastro.html")


@app.route("/cadastro", methods=["POST"])
def submit_cadastro():
    forms = request.form
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM agenda_usuario")
    myresult = mycursor.fetchall()
    for x in myresult:
        if(x[2] == forms['uemail']):
            return render_template("cadastro.html")
    if forms['psw'] == forms['confpsw']:
        sql = "INSERT INTO agenda_usuario (usuario_id, usuario_nome, usuario_email, usuario_status, usuario_senha, usuario_nome_user) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (len(myresult) + 1, forms['uname'], forms['uemail'], 0, forms['psw'], forms['uname'])
        mycursor.execute(sql, val)
        mydb.commit()
        return render_template("login.html")
    else:
        return render_template("cadastro.html")
    
@app.route("/logout", methods=["POST"])
def logout():
    mycursor = mydb.cursor()
    if request.method == 'POST':
        sql = f"UPDATE agenda_usuario SET usuario_status = 0 WHERE usuario_id = {id}"
        mycursor.execute(sql)

    mydb.commit()
    return redirect("/")

@app.route("/delete", methods=["POST"])
def delete():
    mycursor = mydb.cursor()
    if request.method == 'POST':
        sql = f"UPDATE agenda_usuario SET usuario_status = 2 WHERE usuario_id = {id}"
        mycursor.execute(sql)
        
    mydb.commit()
    return redirect("/")

@app.route("/edit", methods=["GET"])
def edit_page():
    return render_template("editar.html")

@app.route("/edit", methods=["POST"])
def edit_user():
    forms = request.form
    if forms['psw'] == forms['confpsw']:
        mycursor = mydb.cursor()
        if request.method == 'POST':
            sql = f"""
            UPDATE agenda_usuario 
            SET usuario_nome = {forms['uanme']},  usuario_email = {forms['uemail']}, usuario_senha = {forms['psw']}, usuario_nome_user = {forms['uanme']}
            WHERE usuario_id = {id}"""

            mycursor.execute(sql)
            mydb.commit()
            return redirect("/home")
    else:
        return render_template("editar.html")



# CALENDARIO
@app.route("/calendario/evento", methods=["GET"])
def evento():
    return render_template("home.html")


@app.route("/calendario/evento", methods=["POST"])
def submit_evento():
    return render_template("home.html")

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == "__main__":
    app.run(host=get_ip(), port=5000, debug=False, threaded=True)
