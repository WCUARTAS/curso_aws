from database.db import *
from controller.s3_administrator import *
from flask import render_template, request
from datetime import datetime

def fun_register():
    db = get_db()
    cursor = db.cursor()
    try:
        
        name = request.form['name']
        phone = request.form['phone']
        birthdate = request.form['birthdate']
        gender = request.form['gender']
        photo = request.files['photo'] 

        extension = photo.filename.split(".")[-1]
        nowDate = datetime.now()
        photo_name = 'photo-'+nowDate.strftime("%Y%m%d%H%M%S")+"."+extension
        


        cursor.execute(
            "INSERT INTO users (name, phone,birthdate,gender,photo) VALUES (%s, %s,%s, %s, %s)",
            (name, phone,birthdate,gender,photo_name)
        )
        db.commit()
        cursor.close()
 

        session_s3 = conectio_s3()
        #photo_path = save_file(photo,photo_name)
        upload_file(session_s3,photo,photo_name)

        return "Registro exitoso!"
    except Exception as e:
        db.rollback()
        cursor.close()
        return f"Error Guardando registro:: {e}"

def fun_getUsers():

    db = get_db()
    cursor = db.cursor()
    try:
        cursor.execute("SELECT name, phone, birthdate, gender,photo FROM users")
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
            list_users.append((user[0], user[1], user[2], translated_gender,user[4]))

    except Exception as e:
        users = []
        print(f"Error al consultar la base de datos: {e}")
    finally:
        cursor.close()

    return render_template('list_users.html', users=list_users)