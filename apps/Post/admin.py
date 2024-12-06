from django.contrib import admin
from apps.Post.models import PostModel, FavModel

admin.site.register(PostModel)
admin.site.register(FavModel)
