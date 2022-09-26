from ..database.db import db

class Todo(db.Model):
    id = db.Column(db.String(80), primary_key=True)
    description = db.Column(db.String(120), unique=True, nullable=False)
    completed = db.Column(db.Boolean, nullable=False)
    username = db.Column(db.String(80), db.ForeignKey('user.username'), nullable=False)

    def __init__(self, id, description, completed, username):
        self.id = id
        self.description = description
        self.completed = completed
        self.username = username
