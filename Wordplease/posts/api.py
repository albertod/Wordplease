from django.contrib.admin import filters
from django.db.models import Q
from .permissions import IsOwnerOrReadOnly
from .models import Blog, Post
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import BlogSerializer, PostSerializer, PostReadSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status, serializers
from .permissions import IsOwnerOrReadOnly
from rest_framework import permissions
from .views import PostsQueryset

#APIS

class BlogsList(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('user__username', )
    ordering_fields = ('user__username', )


class PostListAPI(PostsQueryset, generics.ListCreateAPIView):

    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title', 'summary', )
    ordering_fields = ('title', 'date_published')

    def post(self, request):
        if request.user.is_authenticated():
            serializer_class = PostSerializer
            serializer = PostSerializer(data=request.data, context={'user': request.user})
            if serializer.is_valid():
                new_post = serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            raise serializers.ValidationError("Have to be authenticated to create a post")

    def get_queryset(self):
        serializer_class = PostReadSerializer
        return self.get_posts_queryset(self.request)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PostSerializer
        if self.request.method == 'GET':
            return PostReadSerializer
        return PostSerializer



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