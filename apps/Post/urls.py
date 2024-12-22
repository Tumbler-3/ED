from django.urls import path
from apps.Post.views import PostViewAPI, PostDetailViewAPI, ImagePostViewAPI, ImagePostDetailViewAPI,AuthorPostViewAPI


urlpatterns = [
    path('post/', PostViewAPI.as_view()),
    path('post/author/<int:id>/', AuthorPostViewAPI.as_view()),
    path('post/<int:id>/', PostDetailViewAPI.as_view()),
    path('post/<int:id>/images/', ImagePostViewAPI.as_view()),
    path('post/<int:id>/images/<int:pk>/', ImagePostDetailViewAPI.as_view()),
]
