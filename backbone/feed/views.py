from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponse


def home(request, template='home.html'):
    c = {}
    return render_to_response(template, c, context_instance=RequestContext(request))

"""
@app.route('/post', methods=['PUT','POST',])
def put_post():
    args = json.loads(request.data)
    _id = args.get('_id')
    text = args.get('text')
    if _id:
        post = collection.find_one({'_id': ObjectId(_id)})
        post['text'] = str(text)
        collection.Post.save(post)
    else:
        post = collection.Post()
        post['text'] = str(text)
        post.save()
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
"""