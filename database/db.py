import pymysql

db_host = "rds-test.c104my0q4c00.us-east-1.rds.amazonaws.com"
db_user ="admin"
db_password = "1234567890"
db_database = "db_aws"

try:
    connection = pymysql.connect(
        host = db_host,
        user = db_user,
        password = db_password,
        database = db_database,
        port=3306
    )
    print("conexion exitosa")

    # Crear un cursor para ejecutar la consulta
    with connection.cursor() as cursor:
        # Definir la consulta SQL
        sql_query = "SELECT * FROM users"  # Reemplaza "tu_tabla" con el nombre real de la tabla

        # Ejecutar la consulta
        cursor.execute(sql_query)

        # Obtener todos los resultados
        resultados = cursor.fetchall()

        # Procesar los resultados
        for fila in resultados:
            print(fila)  # Imprime cada fila (cada fila es una tupla)


except Exception as err:
    print("error en conexion a DB:  ",err)

finally:
    # Cerrar la conexión
    if connection:
        connection.close()
        print("Conexión cerrada")