from mongokit import Document
class Post(Document):
    structure = {
        'text': str,
        }

    use_dot_notation = True
    def __repr__(self):
        return '<Post %r>' % (self.text)