from django.conf.urls import include, url


urlpatterns = [

    url(r'^$', 'posts.views.index', name='index'),

]
