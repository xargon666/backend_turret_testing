from flask import Flask
from dotenv import load_dotenv
from os import environ
from flask_cors import CORS

load_dotenv()
database_uri = environ.get('DATABASE_URL')

app = Flask(__name__)
app.config.update(
    SQLALCHEMY_DATABASE_URI=database_uri,
    SQLALCHEMY_TRACK_MODIFICATIONS=environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
)
app.config['SECRET_KEY']=environ.get('SECRET_KEY')

from .database.db import db
from .routes.main import main_routes
from .routes.users import user_routes

load_dotenv()
database_uri = environ.get('DATABASE_URL')

#use CORS in the app and initialize db
CORS(app)
db.app = app
db.init_app(app)

#register blueprints, so that the app can use them for routing
app.register_blueprint(main_routes)
app.register_blueprint(user_routes)

if __name__ == '__main__':
    port = int(environ.get("PORT", 5001))
    app.run(debug=True, host='0.0.0.0', port=port) 
