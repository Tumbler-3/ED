from rest_framework import serializers
from apps.Post.models import PostModel
from apps.User.models import CustomUser
from apps.Post.permissions import decode_token

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostModel
        fields = '__all__'
        read_only_fields = ['author',]
    
    def create(self, validated_data):
        request = self.context.get('request')
        token = request.headers.get('Authorization').split(' ')[1]
        decoded = decode_token(token)
        print(decoded)
        id = decoded['user_id']
        validated_data['author'] = CustomUser.objects.get(id=id)
        return super().create(validated_data)


class PostDetailSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(required=False, read_only=True)

    class Meta:
        model = PostModel
        fields = "__all__"
