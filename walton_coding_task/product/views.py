from django.shortcuts import render
from .models import Product
from rest_framework import generics
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from .permissions import IsSeller

# Create your views here.


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class ProductCreate(generics.CreateAPIView):
    model = Product
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsSeller]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ProductUpdate(generics.UpdateAPIView):
    model = Product
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsSeller]
