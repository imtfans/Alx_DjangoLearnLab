

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.CustomLoginView.as_view(), name='login'),        # REQUIRED
    path('register/', views.register_view, name='register'),              # REQUIRED
    path('profile/', views.profile_view, name='profile'),                # REQUIRED


    path('', views.PostListView.as_view(), name='post-list'),               # /posts/ (root of app)
    path('posts/new/', views.PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
]
