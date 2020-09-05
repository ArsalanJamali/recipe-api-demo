from rest_framework import viewsets,mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from . import serializers
from core import models

class TagViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.CreateModelMixin):
    authentication_classes=(TokenAuthentication,)
    permission_classes=(IsAuthenticated,)
    queryset=models.Tag.objects.all()
    serializer_class=serializers.TagSerializer

    def get_queryset(self):
        return  self.request.user.tag_set.all()
    
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)
        