from django.db import models
from django.views.decorators.http import require_http_methods

class Post(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now_add=True, db_index=True)
    text = models.TextField()

    def __unicode__(self):
        return '[status] %s' % (self.text)