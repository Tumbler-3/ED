from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from apps.Post.models import PostModel
from apps.Post.serializers import PostSerializer, PostDetailSerializer
from apps.Post.permissions import IsAuthor


class PostViewAPI(ListCreateAPIView):
    permission_classes = [IsAuthor,]
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer


class PostDetailViewAPI(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthor,]
    queryset = PostModel.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'id'