from flask import Blueprint
from src.models import Validation
from flask import Flask, render_template, g, request

cadastro = Blueprint('cadastro', __name__)


@cadastro.route("/cadastro", methods=["GET"])
def cadastro():
    return render_template("cadastro.html")


@cadastro.route("/cadastro", methods=["POST"])
def submit_cadastro():
    forms = request.form
    val = Validation("src/database.db")
    if val.cadastro_val(forms['uname'], forms['uemail'], forms['psw'], forms['confpsw']):
        return render_template("login.html")
    else:
        return render_template("cadastro.html")
