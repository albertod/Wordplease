from .models import Blog, Post
from rest_framework import generics
from .serializers import BlogSerializer

#APIS

class BlogsList(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

