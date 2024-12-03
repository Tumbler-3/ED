from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(verbose_name='Email',
                              blank=False, null=False, unique=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


class PasswordReset(models.Model):
    email = models.EmailField()
    token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
