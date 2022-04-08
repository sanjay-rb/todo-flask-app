from flask import Blueprint, jsonify, request

from app.models import User

user = Blueprint('user', __name__, url_prefix='/user')

@user.route('/signup', methods=['POST'])
def signup():
    data = request.json
    user = User(name=data["name"], email=data["email"], number=data["number"])
    user.signup()
    return data