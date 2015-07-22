from rest_framework import serializers
from .models import Blog, Post

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        field = ('id', 'blog_title')
        exclude = ('user', )

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        field = ('id', 'title', 'summary', 'body', 'image_url', 'date_published', 'category', 'blog__user__username')
