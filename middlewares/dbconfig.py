from flask_mysqldb import MySQL
import os

mysql = MySQL()

def init_mysql(app):
    app.config['MYSQL_HOST'] = os.getenv("HOST")
    app.config['MYSQL_USER'] = os.getenv("USER")
    app.config['MYSQL_PASSWORD'] = os.getenv("PASSWORD")
    app.config['MYSQL_DB'] = os.getenv("DBNAME")
    
    mysql.init_app(app)
    print('connected to db')
