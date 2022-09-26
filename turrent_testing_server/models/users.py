from ..database.db import db

class User(db.Model):
    id = db.Column(db.String(80), primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    passwordConfirmation = db.Column(db.String(80), nullable=False)

    def __init__(self, id, username, email, password, passwordConfirmation):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.passwordConfirmation = passwordConfirmation
