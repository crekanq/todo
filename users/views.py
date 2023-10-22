from django.contrib.auth.models import User
from rest_framework import generics, permissions

from .serializers import UserRegistrationSerializer


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]
