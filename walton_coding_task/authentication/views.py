from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from .models import *
from rest_framework import viewsets


class UserCreate(generics.CreateAPIView):
    model = get_user_model()
    serializer_class = UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
