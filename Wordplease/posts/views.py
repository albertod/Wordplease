from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from .models import Post, Blog
from .forms import NewPostForm
from .serializers import *
from rest_framework import generics
from django.utils.decorators import method_decorator
from django.views.generic import DetailView

from django.contrib.auth.models import User


#MixIn class

class PostsQueryset(object):

    def get_posts_queryset(self, request):
        if not request.user.is_authenticated():
            posts = Post.objects.filter(privacy='PUB')
        elif request.user.is_superuser:
            posts = Post.objects.all()
        else:
            posts = Post.objects.filter(Q(blog__user=request.user) | Q(privacy='PUB'))
        return posts

#URLS

def index(request):
    posts = Post.objects.all().filter(privacy='PUB').order_by('-date_published')
    context = {
        'post_list': posts
    }
    return render(request, 'posts/index.html', context)

def blog_list(request):
    blogs = Blog.objects.all().order_by('user')
    context = {
        'blogs_list': blogs
    }
    return render(request, 'posts/blogs_list.html', context)

def blog_user(request, username):
    blog = Blog.objects.all().filter(user__username=username)
    posts = Post.objects.filter(blog=blog, privacy='PUB')
    context = {
        'posts_list': posts
    }
    return render(request, 'posts/blog_user.html', context)

def post_detail(request, username, pk):
    post = Post.objects.filter(pk=pk)[0]
    context = {
        'post': post,
    }
    return render(request, 'posts/post_detail.html', context)

def new_post(request):

    form = NewPostForm()
    post = Post()
    error_messages = []
    if request.method == 'POST':
        title = request.POST.get('title')
        summary = request.POST.get('summary')
        body = request.POST.get('body')
        image_url = request.POST.get('image_url')
        category = request.POST.get('category')

        # request.user.is_aunhenticated() just to be sure
        if title and summary and body and image_url and category and request.user.is_authenticated():
            #create post and save on data base
            post.title = title
            post.summary = summary
            post.body = body
            post.image_url = image_url
            post.category = category
            post.blog = Blog.objects.filter(user=request.user)[0]
            post.save()
            return redirect('posts:index')
        else:
            error_messages.append("Verify the fields are correct/complete")

            context = {
                'errors': error_messages,
                'newpost_form': form,
            }
    else:
        context = {
            'errors': error_messages,
            'newpost_form': form,
         }

    return render(request, 'posts/new_post.html', context)





