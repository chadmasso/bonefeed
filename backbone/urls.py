from django.conf.urls import patterns, include, url
from django.contrib import admin

from tastypie.api import Api
from backbone.api.resources import PostResource

admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(PostResource())

urlpatterns = patterns('',
    url(r'^private/admin/', include(admin.site.urls)),
    (r'^api/', include(v1_api.urls)),
    url(r'^', include('feed.urls')),

)