from flask import Blueprint, jsonify, request

from app.models import User

user = Blueprint('user', __name__, url_prefix='/user')

@user.route('/signup', methods=['POST'])
def signup():
    data = request.json
    json_payload = {}
    is_user_exist = User.query.filter(User.email == data["email"]).first()
    if is_user_exist:
        json_payload["user_id"] = is_user_exist.id
        json_payload["msg"] = f"User already exist : {is_user_exist}"
        return jsonify(json_payload)
    else:
        new_user = User(name=data["name"], email=data["email"])
        new_user.signup()
        new_user.commit()
        json_payload["user_id"] = new_user.id
        json_payload["msg"] = f"New user created : {new_user}"
        return jsonify(json_payload)

@user.route('/delete', methods=['POST'])
def delete():
    data = request.json
    json_payload = {}
    delete_this_user = User.query.filter(User.id == data["user_id"]).first()
    if delete_this_user:
        delete_this_user.delete()
        delete_this_user.commit()
        json_payload["msg"] = f"User deleted : {delete_this_user}"
        return jsonify(json_payload)
    else:
        json_payload["msg"] = f"User not exist with id : {data['user_id']}"
        return jsonify(json_payload)
