from django.conf.urls import include, url
from . import views
from .api import BlogsList, PostDetailAPI, PostListAPI
from users.api import UserDetailAPI, UserListAPI


urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'blogs/$', views.blog_list, name='blogs'),
    url(r'blogs/(?P<username>\w+)/$', views.blog_user, name='blog_user'),
    url(r'blogs/(?P<username>\w+)/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'new-post$', views.new_post, name='new_post'),

    #API Blogs and posts
    url(r'api/1.0/blogs/$', BlogsList.as_view(), name='blogs_list_api'),
    url(r'api/1.0/posts/$', PostListAPI.as_view(), name='posts_list_api'),
    url(r'api/1.0/posts/(?P<pk>[0-9]+)/$', PostDetailAPI.as_view(), name='post_detail_api'),


    #API Users
    url(r'^api/1.0/users/(?P<pk>[0-9]+)$', UserDetailAPI.as_view(), name='user_detail_api'),
    url(r'^api/1.0/users/$', UserListAPI.as_view(), name='user_list_api'),


]
