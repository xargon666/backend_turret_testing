from turrent_testing_server import db
from turrent_testing_server.models import users

# Clear it all out

db.drop_all()

# Set it back up

db.create_all()
