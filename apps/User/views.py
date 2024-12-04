from apps.User.models import CustomUser
from apps.User.tokens import create_jwt
from django.contrib.auth import authenticate, logout
from django.shortcuts import redirect
from apps.User.serializers import AuthorizationSerializer, RegistrationSerializer, EmailSerializer, ResetPasswordSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.urls import reverse
from django.core.mail import EmailMessage


class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "You're logged in!"})


class AuthorizationViewAPI(APIView):
    def post(self, request):
        serializer = AuthorizationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.validated_data)

        if user:
            tokens = create_jwt(user)
            return Response(data={'tokens': tokens})

        return Response(status=status.HTTP_403_FORBIDDEN)


class RegistrationViewAPI(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        CustomUser.objects.create_user(**serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)


def logout_view(request):
    logout(request)
    return redirect('/api/v1/user/login/')


class ResetPassword(generics.GenericAPIView):
    serializer_class = EmailSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        email = serializer.data["email"]
        user = CustomUser.objects.filter(email=email).first()
        
        if user:
            encoded_pk = urlsafe_base64_encode(force_bytes(user.pk))
            token = PasswordResetTokenGenerator().make_token(user)
            
            reset_url = reverse(
                "reset-password",
                kwargs={"encoded_pk": encoded_pk, "token": token},
            )
            reset_link = f"http://127.0.0.1:8000{reset_url}"

            subject = f'Link to reset your password'
            message = f'Link : {reset_link}'
            
            email = EmailMessage(subject, message, to=(email,))
            email.send()

            return Response(
                {
                    "message":
                    f"Your password reset link send to your email"
                },
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"message": "User doesn't exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class ResetPasswordAPI(generics.GenericAPIView):

    serializer_class = ResetPasswordSerializer

    def patch(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"kwargs": kwargs}
        )
        serializer.is_valid(raise_exception=True)
        
        return Response(
            {"message": "Password reset complete"},
            status=status.HTTP_200_OK,
        )
