from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('home.html')

from app.user.routes import user
from app.todo.routes import todo

app.register_blueprint(user)
app.register_blueprint(todo)