from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from .serializers import (
    UserRegistrationSerializer,
    UserLoginSerializer,
    UserSerializer
)

User = get_user_model()


# ----------------------
# Register View
# ----------------------
class RegisterView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = User.objects.get(id=response.data["id"])
        token, _ = Token.objects.get_or_create(user=user)
        return Response(
            {"user": response.data, "token": token.key},
            status=status.HTTP_201_CREATED
        )


# ----------------------
# Login View
# ----------------------
class LoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, _ = Token.objects.get_or_create(user=user)

        return Response({
            "token": token.key,
            "user_id": user.id,
            "username": user.username
        })


# ----------------------
# Profile View
# ----------------------
class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


# ----------------------
# Follow User
# ----------------------
class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    lookup_field = "id"

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get("id")
        target_user = get_object_or_404(self.get_queryset(), id=user_id)

        if target_user == request.user:
            return Response({"error": "You cannot follow yourself"}, status=400)

        if request.user.following.filter(id=target_user.id).exists():
            return Response({"message": "You already follow this user"}, status=200)

        request.user.following.add(target_user)
        return Response({"message": f"You are now following {target_user.username}"}, status=200)


# ----------------------
# Unfollow User
# ----------------------
class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    lookup_field = "id"

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get("id")
        target_user = get_object_or_404(self.get_queryset(), id=user_id)

        if not request.user.following.filter(id=target_user.id).exists():
            return Response({"error": "You are not following this user"}, status=400)

        request.user.following.remove(target_user)
        return Response({"message": f"You have unfollowed {target_user.username}"}, status=200)
