from flask import Blueprint, request, jsonify, make_response, current_app as app
from ..models import questions
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
            current_user = questions.Questions.query.filter_by(id=data['id']).first()
        except:
            return jsonify({'message': 'token is invalid'})
        return f(current_user, *args, **kwargs)
    return decorator  

@main_routes.route("/questions", methods=["GET", "POST"])
def index():
    if request.method == "GET":

        def todo_serializer(Questions):
            return {
                "id": Questions.id,
                "description": Questions.description,
                "completed": Questions.completed,
                "username": Questions.username
            }
        all_todos = questions.Questions.query.all()
        return jsonify([*map(todo_serializer, all_todos)]),200
    else:
        content = request.json
        Questions = questions.Questions(
            id = f'{uuid.uuid1()}',
            description = content["description"],
            completed = content["completed"],
            username = content["username"]
        )
        db.session.add(Questions)
        db.session.commit()
        return jsonify({"message": "Questions created successfully."}), 201

@main_routes.route("/questions/<id>", methods=["GET","PUT", "DELETE"])
def change_todo(id):
    if request.method == "PUT":
        content = request.json
        Questions = questions.Questions.query.filter_by(id=id).first()
        # Questions.description = content["description"]
        Questions.completed = content["completed"]
        db.session.commit()
        return jsonify({"message": "Questions updated successfully."}), 200
    elif request.method == "GET":
        Questions = questions.Questions.query.filter_by(id=id).first()
        return jsonify({"id": Questions.id, "description": Questions.description, "completed": Questions.completed, "username": Questions.username}), 200
    else:
        Questions = questions.Questions.query.filter_by(id=id).first()
        db.session.delete(Questions)
        db.session.commit()
        return jsonify({"message": "Questions deleted successfully."}), 200
