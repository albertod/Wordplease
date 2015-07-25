from django.contrib.auth.models import User
from django.forms import fields
from rest_framework import serializers
from .models import Blog, Post

class BlogSerializer(serializers.ModelSerializer):

    url = serializers.CharField(source="get_absolute_url")

    class Meta:
        model = Blog
        field = ('id', 'blog_title')
        read_only_fields = ('url', )
        exclude = ('user', )



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        field = ('id', 'title', 'summary', 'body', 'image_url', 'date_published', 'category',)
        read_only_field = ('blog',)
        depth = 1

    def create(self, validated_data):
        instance = Post()
        instance.blog = Blog.objects.filter(user=self.context['user'])[0]
        return self.update(instance, validated_data)

    def update(self, instance, validated_data):

        instance.title = validated_data.get('title', instance.title)
        instance.summary = validated_data.get('summary', instance.summary)
        instance.body = validated_data.get('body', instance.body)
        instance.image_url = validated_data.get('image_url',instance.image_url)
        instance.privacy = validated_data.get('privacy', instance.privacy)
        instance.save()
        return instance

    def validate_title(self, data):
        post = Post.objects.filter(title=data)
        # Check if post wth that name already exist
        if post:
            raise serializers.ValidationError("There is a post with that name")
        else:
            return data

    def validate(self, data):
        if Blog.objects.filter(user=self.context['user']).exists():
            return Blog.objects.filter(user=self.context['user'])[0]
        else:
            raise serializers.ValidationError("This users has not a blog registered in the platform")

#Serializer solo usado para leer los articulos (title, imagen, summary and date)
class PostReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        field = ('id', 'title', 'summary', 'image_url', 'date_published',)
        exclude = ('body', 'category','blog',)

