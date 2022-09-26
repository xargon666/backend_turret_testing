from ..database.db import db

class Questions(db.Model):
    id = db.Column(db.String(80), primary_key=True)
    function = db.Column(db.String(300), unique=True, nullable=False)
    test = db.Column(db.String(300), unique=True, nullable=False)
    # username = db.Column(db.String(80), db.ForeignKey('user.username'), nullable=False)

    def __init__(self, id, description, completed, username):
        self.id = id
        self.description = description
        self.completed = completed
        # self.username = username
