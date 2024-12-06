from django.db import models
from apps.User.models import CustomUser


class PostModel(models.Model):
    title = models.CharField(verbose_name='title', max_length=150, null=False)
    content = models.TextField(verbose_name='content', null=False)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='author')
    image = models.ImageField(verbose_name='image', null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='created_at', auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(verbose_name='updated_at', auto_now=True,null=True, blank=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title


class FavModel(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='author')
    post = models.ManyToManyField(PostModel, verbose_name='post')
    created_at = models.DateTimeField(verbose_name='created_at', auto_created=True)

    class Meta:
        verbose_name = 'Favorite'
        verbose_name_plural = 'Favorites'

    def __str__(self):
        return f'{self.author} favorite posts'