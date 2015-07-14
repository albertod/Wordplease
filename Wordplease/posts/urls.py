from django.conf.urls import include, url
from . import views

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'blogs$', views.blog_list, name='blogs'),
    url(r'blogs/(?P<username>\w+)$', views.blog_user, name='blog_user'),
    url(r'blogs/(?P<username>\w+)/(?P<pk>[0-9]+$)', views.post_detail, name='post_detail'),
    url(r'new-post$', views.new_post, name='new_post'),
]
