from rest_framework import serializers
from rest_framework.response import Response
from apps.Post.models import PostModel, PostImageModel
from apps.User.models import CustomUser
from apps.Post.permissions import decode_token


class PostImageSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(required=False, read_only=True)
    thumbnail = serializers.ImageField(read_only=True)

    class Meta:
        model = PostImageModel
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()
    
    def get_author_name(self, obj):
        return f'{obj.author.username}'
    images = PostImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(), write_only=True, required=False)

    class Meta:
        model = PostModel
        fields = "__all__"
        read_only_fields = ['author',]

    def create(self, validated_data):
        request = self.context.get('request')
        try:
            token = request.headers.get('Authorization').split(' ')[1]
        except:
            raise serializers.ValidationError(
                {"detail": "Authentication credentials were not provided."})
        decoded = decode_token(token)
        id = decoded['user_id']
        validated_data['author'] = CustomUser.objects.get(id=id)

        try:
            uploaded_images = validated_data.pop("uploaded_images")
            post = PostModel.objects.create(**validated_data)
            for image in uploaded_images:
                post_image = PostImageModel.objects.create(
                    post=post, image=image)
        except:
            post = PostModel.objects.create(**validated_data)

        return post


class PostDetailSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(required=False, read_only=True)
    images = PostImageSerializer(many=True, read_only=True)
    author_name = serializers.SerializerMethodField()
    
    def get_author_name(self, obj):
        return f'{obj.author.username}'

    class Meta:
        model = PostModel
        fields = "__all__"
