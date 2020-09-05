from . import serializers
from rest_framework import generics,authentication,permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


class CreateUserView(generics.CreateAPIView):
    serializer_class=serializers.UserApiSerializer

class CreateTokenView(ObtainAuthToken):
    serializer_class=serializers.AuthTokenSerializer
    renderer_classes=api_settings.DEFAULT_RENDERER_CLASSES

class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class=serializers.UserApiSerializer
    authentication_classes=(authentication.TokenAuthentication,)
    permission_classes=(permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user