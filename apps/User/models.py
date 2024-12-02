from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(blank=True,null=True, unique=True)
    
    def __str__(self):
        return self.username
