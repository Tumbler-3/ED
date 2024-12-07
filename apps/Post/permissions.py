from rest_framework.permissions import BasePermission, SAFE_METHODS
import jwt
from rest_framework_simplejwt.settings import api_settings


def decode_token(token):
    try:
        decoded_payload = jwt.decode(token, api_settings.SIGNING_KEY, algorithms=[
                                     api_settings.ALGORITHM])
        return decoded_payload
    except:
        return {"error": "Incorrect or expired Token"}


class IsAuthor(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        try:
            token = request.headers.get('Authorization').split(' ')[1]
        except:
            return False
        decoded = decode_token(token)
        id = decoded['user_id']
        try:
            return obj.author.id == id
        except:
            return obj.post.author.id == id