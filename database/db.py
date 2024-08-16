import pymysql
#EC2
db_host = "rds-test.c104my0q4c00.us-east-1.rds.amazonaws.com"
db_user ="admin"
db_password = "1234567890"
db_database = "db_aws"

#LOCAL
""" 
db_host = "127.0.0.1"
db_user ="root"
db_password = ""
db_database = "db_aws"
"""

def get_db():
    try:
        connection = pymysql.connect(
            host = db_host,
            user = db_user,
            password = db_password,
            database = db_database,
            port=3306
        )
        print("conexion exitosa")
        return connection
    except Exception as err:
        print("error en conexion a DB:  ",err)
        return null
