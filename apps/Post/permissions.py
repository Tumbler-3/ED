from rest_framework.permissions import BasePermission
import jwt
from rest_framework_simplejwt.settings import api_settings


def decode_token(token):
    try:
        decoded_payload = jwt.decode(token, api_settings.SIGNING_KEY, algorithms=[api_settings.ALGORITHM])
        return decoded_payload
    except:
        return {"error": "Incorrect or expired Token"}

    
class IsAuthor(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True 
        token = request.headers.get('Authorization').split(' ')[1]
        decoded = decode_token(token)
        id = decoded['user_id']
        return obj.author.id == id
