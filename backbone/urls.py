from django.conf.urls import patterns, include, url

from tastypie.api import Api
from backbone.api.resources import PostResource

v1_api = Api(api_name='v1')
v1_api.register(PostResource())

urlpatterns = patterns('',
    (r'^api/', include(v1_api.urls)),
    url(r'^', include('feed.urls')),
)