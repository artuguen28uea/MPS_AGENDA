import sqlite3
import random
from flask import Flask, render_template, g, request
from src.models import Validation

app = Flask(__name__)
app.secret_key = "dosfjdsofjoskjeicds_Sd"

# LOGIN

@app.route("/", methods=["GET"])
def login():
    return render_template("login.html")

@app.route("/", methods=["POST"])
def submit_login():
    forms = request.form
    val = Validation("src/database.db")
    if val.login_val(forms['uemail'], forms['pwd']):
        return render_template("home.html")
    else:
        return render_template("login.html")

# CADASTRO

@app.route("/cadastro", methods=["GET"])
def cadastro():
    return render_template("cadastro.html")

@app.route("/cadastro", methods=["POST"])
def submit_cadastro():
    forms = request.form
    val = Validation("src/database.db")
    if val.cadastro_val(forms['uname'], forms['uemail'], forms['psw'], forms['confpsw']):
        return render_template("login.html")
    else:
        return render_template("cadastro.html")

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


if __name__ == '__main__':
    app.run()
