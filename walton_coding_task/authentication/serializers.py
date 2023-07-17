from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ["id", "email", "phone", "age", "gender",
                  "name", "is_customer", "is_seller", "password"]

    def create(self, validated_data):
        user = CustomUser.objects.create(email=validated_data['email'],
                                         phone=validated_data['phone'],
                                         age=validated_data['age'],
                                         gender=validated_data['gender'],
                                         is_customer=validated_data['is_customer'],
                                         is_seller=validated_data['is_seller'],

                                         )
        user.set_password(validated_data['password'])
        user.save()
        return user
