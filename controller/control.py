from database.db import *
from controller.s3_administrator import conectio_s3
from flask import render_template, request

def fun_register():
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
        
        #conectio_s3()
        return "Registro exitoso!"
    except Exception as e:
        db.rollback()
        cursor.close()
        return f"Error Guardando registro:: {e}"

def fun_getUsers():

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