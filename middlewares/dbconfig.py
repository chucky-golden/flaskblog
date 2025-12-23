from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def init_db(app):
    user = os.getenv("USER")
    password = os.getenv("PASSWORD")
    host = os.getenv("HOST")
    dbname = os.getenv("DBNAME")

    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f"mysql+pymysql://{user}:{password}@{host}/{dbname}"
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    print("Connected to database with SQLAlchemy")
