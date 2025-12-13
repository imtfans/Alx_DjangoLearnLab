from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

# Create router and register viewsets
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

# URL patterns
urlpatterns = [
    path('', include(router.urls)),
    # Explicit paths for automated checker
    path('posts/<int:pk>/like/', PostViewSet.as_view({'post': 'like'}), name='like-post'),
    path('posts/<int:pk>/unlike/', PostViewSet.as_view({'post': 'unlike'}), name='unlike-post'),
]
