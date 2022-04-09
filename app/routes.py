from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('home.html')

from app.user.routes import user

app.register_blueprint(user)