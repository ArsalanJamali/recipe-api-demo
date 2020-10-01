from rest_framework import viewsets,mixins,status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from . import serializers
from core import models
from rest_framework.decorators import action 
from rest_framework.response import Response


class TagViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.CreateModelMixin):
    authentication_classes=(TokenAuthentication,)
    permission_classes=(IsAuthenticated,)
    queryset=models.Tag.objects.all()
    serializer_class=serializers.TagSerializer

    def get_queryset(self):
        return  self.request.user.tag_set.all()
    
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)
        
class IngredientViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.CreateModelMixin):
    queryset=models.Ingredient.objects.all()
    permission_classes=(IsAuthenticated,)
    authentication_classes=(TokenAuthentication,)        
    serializer_class=serializers.IngredientSerializer

    def get_queryset(self):
        return self.request.user.ingredient_set.all()

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

class RecipeViewset(viewsets.ModelViewSet):
    queryset=models.Recipe.objects.all()
    serializer_class=serializers.RecipeSerializer
    authentication_classes=(TokenAuthentication,)
    permission_classes=(IsAuthenticated,)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)    

    def get_serializer_class(self):

        if self.action == 'retrieve':
            return serializers.RecipeDetailSerializer
        elif self.action == 'upload_image':
            return serializers.RecipeImageSerializer
        else:
            return self.serializer_class    

    @action(methods=['POST'],url_path='upload-image',detail=True)
    def upload_image(self,request,pk=None):
        recipe_obj=self.get_object()
        serializer=self.get_serializer(recipe_obj,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    





    
    