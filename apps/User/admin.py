from django.contrib import admin
from apps.User.models import CustomUser

admin.site.register(CustomUser)