from .permissions import IsOwnerOrReadOnly
from .models import Blog, Post
from rest_framework import generics
from .serializers import BlogSerializer, PostSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from .permissions import IsOwnerOrReadOnly
from rest_framework import permissions

#APIS

class BlogsList(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class PostListAPI(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailAPI(generics.GenericAPIView):

    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        self.check_object_permissions(request, post)  # compruebo si el usuario autenticado puede hacer GET en este user
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        self.check_object_permissions(request, post)  # compruebo si el usuario autenticado puede hacer PUT en este user
        serializer = PostSerializer(instance=post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        self.check_object_permissions(request, post)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)