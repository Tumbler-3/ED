from django.db import models
from apps.User.models import CustomUser
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class PostModel(models.Model):
    title = models.CharField(verbose_name='title', max_length=150, null=False)
    content = models.TextField(verbose_name='content', null=False)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='author')
    created_at = models.DateTimeField(verbose_name='created_at', auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(verbose_name='updated_at', auto_now=True,null=True, blank=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title

class PostImageModel(models.Model):
    post = models.ForeignKey(PostModel, verbose_name='post', related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True, upload_to='post_img')
    thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(100, 50)], format='JPEG', options={'quality': 60})

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    def __str__(self):
        return f'Image of {self.post.title}'

class FavModel(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='author')
    post = models.ManyToManyField(PostModel, verbose_name='post')
    created_at = models.DateTimeField(verbose_name='created_at', auto_created=True)

    class Meta:
        verbose_name = 'Favorite'
        verbose_name_plural = 'Favorites'

    def __str__(self):
        return f'{self.author} favorite posts'