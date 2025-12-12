from rest_framework import viewsets, permissions, filters, generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

# ----------------------
# Custom Permissions
# ----------------------
class IsAuthorOrReadOnly(permissions.BasePermission):
    """Custom permission to allow only authors to edit or delete their content."""
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user

# ----------------------
# Post ViewSet
# ----------------------
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['title', 'content']
    filterset_fields = ['author__username']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# ----------------------
# Comment ViewSet
# ----------------------
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# ----------------------
# Feed View
# ----------------------
class FeedView(generics.ListAPIView):
    """List posts from users that the current user is following."""
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # Make sure your User model has a 'following' ManyToMany field
        return Post.objects.filter(author__in=user.following.all()).order_by('-created_at')
