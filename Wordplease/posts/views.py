from django.shortcuts import render
from .models import Post, Blog

def index(request):
    posts = Post.objects.all().order_by('-date_published')
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
    posts = Post.objects.filter(blog=blog)
    context = {
        'posts_list': posts
    }
    return render(request, 'posts/blog_user.html', context)

def post_detail(request, pk):
    post = Post.objects.filter(pk=pk)
    context = {
        'post': post
    }
    return render(request, 'posts/post_detail.html', context)
