from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    password = models.CharField(max_length=50, null=True)
    
    email = models.EmailField(max_length=254, unique=True, default="")
    username = models.CharField(max_length=50, default="")
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.get_full_name()