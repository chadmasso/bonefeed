from backbone import app
from flask import url_for, render_template, request
from backbone.models import Post
from backbone.db import connection
from tools import jsonify
import json

with app.test_request_context():
    url_for('static', filename='css/style.css')
    url_for('static', filename='js/backbone-min.js')
    url_for('static', filename='js/app.js')
    url_for('static', filename='js/underscore-min.js')
    url_for('static', filename='js/zepto.min.js')

collection = connection['test'].posts

@app.route('/', methods=['GET',])
def index():
    c = {}
    return render_template('home.html', **c)

@app.route('/post', methods=['PUT',])
def put_post():
    post = collection.Post()
    args = json.loads(request.data)
    post['text'] = str(args['text'])
    post.save()
    print "hmm"
    return jsonify(post)

@app.route('/posts', methods=['GET',])
def get_posts():
    posts = collection.Post.find()
    return jsonify(posts = list(posts))

@app.route('/posts/<int:post_id>', methods=['GET',])
def get_post(post_id):
    c = {}
    c['id'] = post_id
    c['text'] = "coffee is what i need"
    return jsonify(c)

