from django.urls import path
from rest_framework.routers import DefaultRouter
from django.urls import path,  include
from .views import *

router = DefaultRouter()
# router.register(r'users', UserViewSet)

urlpatterns = [
    # path('api/', include(router.urls)),
    path('api/product_list/', ProductList.as_view(), name="product_list"),
    path('api/product_create/', ProductCreate.as_view(), name="product_create"),
    path('api/product_update/<int:pk>',
         ProductUpdate.as_view(), name="product_create"),
]
