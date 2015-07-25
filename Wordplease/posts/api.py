from django.db.models import Q
from .permissions import IsOwnerOrReadOnly
from .models import Blog, Post
from rest_framework import generics
from .serializers import BlogSerializer, PostSerializer, PostReadSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status, serializers
from .permissions import IsOwnerOrReadOnly
from rest_framework import permissions

#APIS

class BlogsList(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class PostListAPI(generics.ListAPIView):

    #serializer_class = PostReadSerializer

    def post(self, request):
        if request.user.is_authenticated():
            serializer = PostSerializer(data=request.data, context={'user': request.user})
            if serializer.is_valid():
                new_post = serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            raise serializers.ValidationError("HAve to be authenticated to create a post")

    def get_queryset(self):
        user = self.request.user
        serializers = PostReadSerializer
        if user.is_superuser:
            return Post.objects.all()
        elif user.is_active:
            from_user = Post.objects.filter(blog__user=user)
            public_post = Post.objects.filter(~Q(blog__user=user), privacy='PUB')
            return from_user | public_post # this add together the results of the queryes
        else:
            return Post.objects.all().filter(privacy='PUB')

    def get_serializer_class(self):
        if self.action == 'post':
            return PostSerializer
        if self.action == 'get_query_set':
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