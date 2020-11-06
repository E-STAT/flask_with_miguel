from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate 


app = Flask(__name__)
app.config.from_object(Config)


from app import routes

