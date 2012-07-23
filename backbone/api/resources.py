from tastypie import fields
from tastypie.resources import ModelResource
from feed.models import Post, Comment
from tastypie.authorization import Authorization


class PostResource(ModelResource):
    comments = fields.ToManyField('backbone.api.resources.CommentResource', 'comment_set', full=True, blank=True,  related_name='post')

    class Meta:
        queryset = Post.objects.all()
        resource_name = 'post'
        always_return_data = True
        authorization = Authorization()

class CommentResource(ModelResource):
    post = fields.ToOneField(PostResource, 'post')

    class Meta:
        queryset = Comment.objects.all()
        resource_name = 'comment'
        always_return_data = True
        authorization = Authorization()


