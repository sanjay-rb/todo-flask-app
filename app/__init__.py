from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

from dotenv import load_dotenv
load_dotenv('.env') 

databse_uri = os.environ.get('DB_URL')
app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = databse_uri

db = SQLAlchemy(app)

from app import routes, models