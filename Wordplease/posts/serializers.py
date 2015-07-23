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


    def update(self, instance, validated_data):
        """
        Actualiza una instancia de Post a partir de los datos
        del dicccionario validated_data que contiene valores deserializados
        :param instance: objeto Post a actualizar
        :param validated_data: diccionario con nuevos valores para el Post
        :return: objeto Post actualizado
        """
        instance.title = validated_data.get('title')
        instance.summary = validated_data.get('summary')
        instance.body = validated_data.get('body')
        instance.image_url = validated_data.get('image_url')
        instance.save()
        return instance