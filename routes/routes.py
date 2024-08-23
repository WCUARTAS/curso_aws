from server import app
from flask import render_template
from controller.control import *

@app.route("/")
def test_page():
    return "<h1>Hola Mundo</h1>"

@app.route("/register_page")
def register_page():
    return render_template("register.html")

# ruta para insertar datos
@app.route('/save', methods=['POST'])
def register():
    return fun_register()


# ruta para consultar los datos
@app.route('/list_users', methods=['GET'])
def getUsers():
    return fun_getUsers()