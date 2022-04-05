# from msilib import Table
import os
from xmlrpc.client import DateTime
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_mysqldb import MySQL
import MySQLdb.cursors
from sqlalchemy import Table, Column, Integer, String, MetaData
from datetime import datetime
from sqlalchemy import create_engine, text
from sqlalchemy.sql import func
db = SQLAlchemy()
# db = MySQL()
migrate = Migrate()
ma = Marshmallow()
cors = CORS()
load_dotenv()


def create_app():
    app = Flask(__name__)
    # app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:admin123@localhost/article_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    meta = MetaData()
    engine = create_engine('mysql://root:admin123@localhost/article_db')

    articles = Table(
        'articles', meta,
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('title', String(100), nullable=False),
        Column('body', String(300), nullable=False),
    )
    meta.create_all(engine)
    # Enter your database connection details below
    # app.config['MYSQL_HOST'] = 'localhost'
    # app.config['MYSQL_USER'] = 'root'
    # app.config['MYSQL_PASSWORD'] = 'admin123'
    # app.config['MYSQL_DB'] = 'article_db'

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    cors.init_app(app)

    return app
