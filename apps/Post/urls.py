from django.urls import path
from apps.Post.views import PostViewAPI, PostDetailViewAPI


urlpatterns = [
    path('post/', PostViewAPI.as_view()),
    path('post/<int:id>/', PostDetailViewAPI.as_view()),
]
