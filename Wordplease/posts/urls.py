from django.conf.urls import include, url


urlpatterns = [

    url(r'^$', 'posts.views.index', name='index'),
    url(r'blogs$', 'posts.views.blog_list', name='blogs'),
    url(r'blogs/(?P<username>\w+)$', 'posts.views.blog_user', name='blog_user'),
    url(r'blogs/(?P<username>\w+)/(?P<pk>[0-9]+$)', 'posts.views.post_detail', name='post_detail'),

]
