from django.conf.urls import patterns

urlpatterns = patterns('',
    (r'^$', 'feed.views.home', {}, 'home'),

)
