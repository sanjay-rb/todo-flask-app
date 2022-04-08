from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

databse_uri = os.environ.get('DB_URL')
app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = databse_uri

db = SQLAlchemy(app)


@app.route('/')
def index():
    return "Hi Sanjay"