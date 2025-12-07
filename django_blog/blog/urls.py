from django.urls import path
from .views import (
    home,
    register_view,
    CustomLoginView,
    CustomLogoutView,
    profile_view,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
)

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('home/', home, name='home'),

    # User Auth
    path('register/', register_view, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', profile_view, name='profile'),

    # Posts
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # Comments
    path(
        'post/<int:post_pk>/comment/new/',
        CommentCreateView.as_view(),
        name='comment-create'
    ),
    path(
        'comment/<int:pk>/edit/',
        CommentUpdateView.as_view(),
        name='comment-edit'
    ),
    path(
        'comment/<int:pk>/delete/',
        CommentDeleteView.as_view(),
        name='comment-delete'
    ),
]
