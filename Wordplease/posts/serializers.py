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
        read_only_fields = ("blog",)
        depth = 1

    def update(self, instance, validated_data):

        instance.title = validated_data.get('title', instance.title)
        instance.summary = validated_data.get('summary', instance.summary)
        instance.body = validated_data.get('body', instance.body)
        instance.image_url = validated_data.get('image_url',instance.image_url)
        instance.privacy = validated_data.get('privacy', instance.privacy)
        instance.save()
        return instance

#Serializer solo usado para leer los articulos (title, imagen, summary and date)
class PostReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        field = ('id', 'title', 'summary', 'image_url', 'date_published',)
        exclude = ('body', 'category','blog',)

