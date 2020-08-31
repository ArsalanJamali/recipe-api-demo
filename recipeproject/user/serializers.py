from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserApiSerializer(serializers.ModelSerializer):

    class Meta:
        model=get_user_model()
        fields=('id','name','email','password')

        extra_kwargs={
            'password':{
            'write_only':True,
            'min_length':5,
            'style':{'input_type':'password'}
            }
        }

    def create(self,validated_data):
        return get_user_model().objects.create_user(**validated_data)

    def update(self,instance,validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.email=validated_data.get('email',instance.email)
        instance.set_password(validated_data.get('password',instance.password))
        instance.save()
        return instance   








