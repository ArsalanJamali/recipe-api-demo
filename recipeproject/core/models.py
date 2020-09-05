from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,BaseUserManager)
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from django.conf import settings

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

    def __str__(self):
        return self.name

        







