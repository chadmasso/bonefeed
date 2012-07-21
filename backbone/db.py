from backbone import app
from backbone.models import Post
from mongokit import Connection

# connect to the database
connection = Connection(app.config['MONGODB_HOST'],
    app.config['MONGODB_PORT'])

# register the User document with our current connection
connection.register([Post])