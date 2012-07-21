from tastypie.resources import ModelResource
from feed.models import Post
from tastypie.authorization import Authorization

class PostResource(ModelResource):
    class Meta:
        queryset = Post.objects.all()
        resource_name = 'post'
        always_return_data = True
        authorization = Authorization()

    def hydrate(self, bundle):
        print "hydrating"
        return bundle