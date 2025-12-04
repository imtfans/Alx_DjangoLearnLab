

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.CustomLoginView.as_view(), name='login'),        # REQUIRED
    path('register/', views.register_view, name='register'),              # REQUIRED
    path('profile/', views.profile_view, name='profile'),                # REQUIRED
]
