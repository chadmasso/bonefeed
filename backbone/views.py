from backbone import app
from flask import url_for, render_template, request, jsonify

with app.test_request_context():
    url_for('static', filename='css/style.css')
    url_for('static', filename='js/backbone-min.js')
    url_for('static', filename='js/app.js')
    url_for('static', filename='js/underscore-min.js')
    url_for('static', filename='js/zepto.min.js')

@app.route('/', methods=['GET',])
def index():
    c = {}
    return render_template('home.html', **c)

@app.route('/posts', methods=['GET',])
def get_posts():
    posts = [{'id': 123, 'text': "coffee is what i need"}, {'id': 124, 'text': "i need it now!"},]
    return jsonify(posts = posts)

@app.route('/posts/<int:post_id>', methods=['GET',])
def get_post(post_id):
    c = {}
    c['id'] = post_id
    c['text'] = "coffee is what i need"
    return jsonify(c)

