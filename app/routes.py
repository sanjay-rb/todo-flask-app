from app import app

@app.route('/')
def index():
    return "Hi Sanjay"

from app.user.routes import user

app.register_blueprint(user)