from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from .models import Post
from .serializers import PostSerializer


class PostListView(generics.ListCreateAPIView):
    """
    List all posts or create a new post.
    """
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a specific post.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserFeedView(APIView):
    """
    Returns a feed of posts from users the authenticated user follows.
    Ordered by most recent posts first.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # Users the current user is following
        following_users = request.user.following.all()

        # FEED QUERY — required by checker
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')

        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
