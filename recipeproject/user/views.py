from . import serializers
from rest_framework import generics

class CreateUserView(generics.CreateAPIView):
    serializer_class=serializers.UserApiSerializer



