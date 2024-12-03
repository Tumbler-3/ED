from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(verbose_name='Email',blank=False,null=False, unique=True)
    created_at = models.TimeField(auto_now=True)
    
    def __str__(self):
        return self.username
