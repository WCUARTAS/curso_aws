from flask import Flask, render_template, request
from database.db import get_db

app = Flask(__name__)

@app.route("/")
def test_page():
    return "<h1>Hola Mundo</h1>"

@app.route("/register_page")
def register_page():
    return render_template("register.html")

# ruta para insertar datos
@app.route('/save', methods=['POST'])
def register():

    db = get_db()
    cursor = db.cursor()
    try:
        data = request.json  # Recibir los datos como JSON
        name = data['name']
        phone = data['phone']
        birthdate = data['birthdate']
        gender = data['gender']

        cursor.execute(
            "INSERT INTO users (name, phone,birthdate,gender) VALUES (%s, %s,%s, %s)",
            (name, phone,birthdate,gender)
        )
        db.commit()
        cursor.close()
        return "Registro exitoso!"
    except Exception as e:
        db.rollback()
        cursor.close()
        return f"Error Guardando registro:: {e}"


# ruta para consultar los datos
@app.route('/list_users', methods=['GET'])
def users():
    db = get_db()
    cursor = db.cursor()
    try:
        cursor.execute("SELECT name, phone, birthdate, gender FROM users")
        users = cursor.fetchall()  # Obtiene todos los registros

        # Traducción de los valores de género al español
        list_users = []
        for user in users:
            translated_gender = {
                'male': 'Masculino',
                'female': 'Femenino',
                'other': 'Otro',
                'prefer_not_to_say': 'Prefiero no decirlo'
            }.get(user[3], 'Desconocido')  # Traducir o dejar 'Desconocido' si no hay coincidencia
            list_users.append((user[0], user[1], user[2], translated_gender))

    except Exception as e:
        users = []
        print(f"Error al consultar la base de datos: {e}")
    finally:
        cursor.close()

    return render_template('list_users.html', users=list_users)

if __name__ == "__main__":
    host = "0.0.0.0"
    port = "80"
    app.run(host,port)