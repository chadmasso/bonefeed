from django.db import models

class Post(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now_add=True, db_index=True)
    text = models.TextField()

    def __unicode__(self):
        return '[status] %s' % (self.text)

class Comment(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    post = models.ForeignKey(Post)

    def __unicode__(self):
        return '[comment] %s' % (self.text)