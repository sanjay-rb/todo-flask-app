from flask import Blueprint, jsonify, request

from app.models import Todo, User

todo = Blueprint('todo', __name__, url_prefix='/todo')

@todo.route('/add', methods=["POST"])
def add():
    data = request.json
    json_payload = {}
    new_todo = Todo(content=data['content'], due_date=data['due_date'], is_completed=data['is_completed'], user_id=data['user_id'])
    new_todo.add()
    new_todo.commit()
    json_payload['todo_id'] = new_todo.id
    json_payload['msg'] = f"New todo added : {new_todo}"
    return jsonify(json_payload), 200

@todo.route('/list', methods=["GET"])
def list():
    data = request.json
    json_payload = {}
    user = User.query.filter(User.id == data['user_id']).first()
    if user:
        json_payload['todos'] = []
        for todo in user.todos:
            json_payload['todos'].append(todo.toJson())
        json_payload['msg'] = f'Todos fetched from {user}'
        return jsonify(json_payload), 200
    else:
        json_payload['todos'] = []
        json_payload['msg'] = f'User not exist with id {data["user_id"]}'
        return jsonify(json_payload), 404

@todo.route('/<int:todo_id>', methods=['GET'])
def get(todo_id):
    json_payload = {}
    todo = Todo.query.filter(Todo.id == todo_id).first()
    if todo:
        json_payload['todo'] = todo.toJson()
        json_payload['msg'] = f"Todo fetched successfully : {todo}"
        return jsonify(json_payload), 200
    else:
        json_payload['msg'] = f"Todo not exist with id : {todo_id}"
        return jsonify(json_payload), 404

@todo.route('/<int:todo_id>/update', methods=['PUT'])
def update(todo_id):
    data = request.json
    json_payload = {}
    update_todo = Todo.query.filter(Todo.id == todo_id).first()
    if update_todo:
        update_todo.content = data['content']
        update_todo.due_date = data['due_date']
        update_todo.is_completed = data['is_completed']
        update_todo.commit()
        json_payload['todo'] = update_todo.toJson()
        json_payload['msg'] = f"Todo updated successfully : {update_todo}"
        return jsonify(json_payload), 200

    else:
        json_payload["msg"] = f"Todo not exist with id : {todo_id}"
        return jsonify(json_payload), 404


@todo.route('/<int:todo_id>/delete', methods=['DELETE'])
def delete(todo_id):
    json_payload = {}
    delete_this_todo = Todo.query.filter(Todo.id == todo_id).first()
    if delete_this_todo:
        delete_this_todo.delete()
        delete_this_todo.commit()
        json_payload["msg"] = f"Todo deleted : {delete_this_todo}"
        return jsonify(json_payload), 200
    else:
        json_payload["msg"] = f"Todo not exist with id : {todo_id}"
        return jsonify(json_payload), 404

