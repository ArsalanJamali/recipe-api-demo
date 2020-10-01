from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,BaseUserManager)
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from django.conf import settings
import os
import uuid


def recipe_image_file_path(instance,filename):

    ext=filename.split('.')[-1]
    filename="{}.{}".format(uuid.uuid4(),ext)
    return os.path.join('uploads/recipe/',filename)



class UserManager(BaseUserManager):

    def create_user(self,email,password=None,**extra_fields):
        
        if not email:
            raise ValueError('Users Must Have an email address')
        user=self.model(email=self.normalize_email(email),**extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,email,password):
        user=self.create_user(email=email,password=password)
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser,PermissionsMixin):

    email=models.EmailField(max_length=254,unique=True)
    name=models.CharField(max_length=100,blank=True)
    is_active=models.BooleanField(default=True)    
    is_staff=models.BooleanField(default=False)
    date_joined=models.DateTimeField(default=timezone.now)

    objects=UserManager()

    USERNAME_FIELD='email'

class Tag(models.Model):
    name=models.CharField(max_length=255)
    user=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)

    class Meta:
        ordering=['-pk']

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name=models.CharField(max_length=255)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    class Meta:
        ordering=['-pk']

    def __str__(self):
        return self.name

class Recipe(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    time_minutes=models.IntegerField()
    price=models.DecimalField(max_digits=5,decimal_places=2)
    link=models.URLField(max_length=200,blank=True)
    ingredients=models.ManyToManyField(Ingredient)
    tags=models.ManyToManyField(Tag)
    image=models.ImageField(null=True,upload_to=recipe_image_file_path,blank=True)
    

    class Meta:
        ordering=['-pk']

    def __str__(self):
        return self.title

    







