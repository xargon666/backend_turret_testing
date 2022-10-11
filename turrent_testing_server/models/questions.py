from turtle import title
from ..database.db import db

class Questions(db.Model):
    id = db.Column(db.String(80), primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    function = db.Column(db.String(300), unique=True, nullable=False)
    jest_function_incomplete = db.Column(db.String(300), unique=True, nullable=False)
    jest_function_complete = db.Column(db.String(300), unique=True, nullable=False)
    description = db.Column(db.String(300), unique=True, nullable=False)
    difficulty = db.Column(db.String(300), unique=True, nullable=False)
    real_function = db.Column(db.String(300), unique=True, nullable=False)
    language = db.Column(db.String(80), unique=True, nullable=False)
    test = db.Column(db.String(300), unique=True, nullable=False)
    # username = db.Column(db.String(80), db.ForeignKey('user.username'), nullable=False)

    def __init__(self, id, description, completed, difficulty, language, test, title, function, jest_function_incomplete, jest_function_complete, real_function):
        self.id = id
        self.description = description
        self.completed = completed
        self.difficulty = difficulty
        self.language = language
        self.test = test
        self.title = title
        self.function = function
        self.jest_function_incomplete = jest_function_incomplete
        self.jest_function_complete = jest_function_complete
        self.real_function = real_function
