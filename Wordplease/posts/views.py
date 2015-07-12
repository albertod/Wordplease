from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.all().order_by('-date_published')
    context = {
        'post_list': posts
    }
    return render(request, 'posts/index.html', context)