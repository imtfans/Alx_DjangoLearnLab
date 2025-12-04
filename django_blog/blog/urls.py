
    

from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

urlpatterns = [
     path('', views.home, name='home'),
    path('login/', views.CustomLoginView.as_view(), name='login'),        # REQUIRED
    path('register/', views.register_view, name='register'),              # REQUIRED
    path('profile/', views.profile_view, name='profile'),                # REQUIRED


    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
