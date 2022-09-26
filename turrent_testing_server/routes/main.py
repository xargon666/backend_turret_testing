from flask import Blueprint, request, jsonify, make_response, current_app as app
from ..models import todos
from ..database.db import db
from functools import wraps
import uuid
import jwt
import datetime

main_routes = Blueprint("main", __name__)

def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']

        if not token:
            return jsonify({'message': 'a valid token is missing'})
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = todos.Todo.query.filter_by(id=data['id']).first()
        except:
            return jsonify({'message': 'token is invalid'})
        return f(current_user, *args, **kwargs)
    return decorator  

@main_routes.route("/todos", methods=["GET", "POST"])
def index():
    if request.method == "GET":

        def todo_serializer(todo):
            return {
                "id": todo.id,
                "description": todo.description,
                "completed": todo.completed,
                "username": todo.username
            }
        all_todos = todos.Todo.query.all()
        return jsonify([*map(todo_serializer, all_todos)]),200
    else:
        content = request.json
        todo = todos.Todo(
            id = f'{uuid.uuid1()}',
            description = content["description"],
            completed = content["completed"],
            username = content["username"]
        )
        db.session.add(todo)
        db.session.commit()
        return jsonify({"message": "Todo created successfully."}), 201

@main_routes.route("/todos/<id>", methods=["GET","PUT", "DELETE"])
def change_todo(id):
    if request.method == "PUT":
        content = request.json
        todo = todos.Todo.query.filter_by(id=id).first()
        # todo.description = content["description"]
        todo.completed = content["completed"]
        db.session.commit()
        return jsonify({"message": "Todo updated successfully."}), 200
    elif request.method == "GET":
        todo = todos.Todo.query.filter_by(id=id).first()
        return jsonify({"id": todo.id, "description": todo.description, "completed": todo.completed, "username": todo.username}), 200
    else:
        todo = todos.Todo.query.filter_by(id=id).first()
        db.session.delete(todo)
        db.session.commit()
        return jsonify({"message": "Todo deleted successfully."}), 200
