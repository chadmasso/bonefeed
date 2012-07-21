from flask import Flask

# configuration
MONGODB_HOST = '0.0.0.0'
MONGODB_PORT = 27017

app = Flask(__name__)
app.config.from_object(__name__)

import backbone.views