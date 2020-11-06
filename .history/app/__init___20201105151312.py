from flask import Flask
from config import Configfrom
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config.from_object(Config)


from app import routes

