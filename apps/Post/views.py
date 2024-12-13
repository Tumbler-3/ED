from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from apps.Post.models import PostModel, PostImageModel
from apps.Post.serializers import PostSerializer, PostDetailSerializer, PostImageSerializer
from apps.Post.permissions import IsAuthor
from django.shortcuts import get_object_or_404, render
from apps.Post.permissions import decode_token

def main(request):
    return render(request, 'main')

class PostViewAPI(ListCreateAPIView):
    permission_classes = [IsAuthor,]
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer


class PostDetailViewAPI(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthor,]
    queryset = PostModel.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'id'


class ImagePostViewAPI(ListCreateAPIView):
    permission_classes = [IsAuthor,]
    serializer_class = PostImageSerializer
    
    def get_queryset(self):
        id = self.kwargs['id']
        post = PostModel.objects.get(id=id)
        return PostImageModel.objects.filter(post=post)
    
    def create(self, request, *args, **kwargs):
        try:
            token = request.headers.get('Authorization').split(' ')[1]
        except:
            raise serializers.ValidationError({"detail": "Authentication credentials were not provided."})
        
        decoded = decode_token(token)
        token_id = decoded['user_id']
        post = get_object_or_404(PostModel, id=self.kwargs['id'])

        if token_id != post.author.pk:
            raise serializers.ValidationError({"detail": "Authentication credentials were not provided."})
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(post=post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ImagePostDetailViewAPI(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthor,]
    serializer_class = PostImageSerializer
    lookup_field = 'pk'
    
    def get_queryset(self):
        id = self.kwargs['id']
        post = PostModel.objects.get(id=id)
        return PostImageModel.objects.filter(post=post)