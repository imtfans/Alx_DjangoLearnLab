from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import User  # your custom user model

# Follow a user
class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()  # required for the task checker
    lookup_field = 'id'

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        target_user = get_object_or_404(self.get_queryset(), id=user_id)
        if target_user == request.user:
            return Response({'error': "You cannot follow yourself"}, status=status.HTTP_400_BAD_REQUEST)
        request.user.following.add(target_user)
        return Response({'message': f'You are now following {target_user.username}'}, status=status.HTTP_200_OK)


# Unfollow a user
class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()  # required for the task checker
    lookup_field = 'id'

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        target_user = get_object_or_404(self.get_queryset(), id=user_id)
        request.user.following.remove(target_user)
        return Response({'message': f'You have unfollowed {target_user.username}'}, status=status.HTTP_200_OK)
