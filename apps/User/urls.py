from django.urls import re_path
from apps.User.views import AuthorizationViewAPI, RegistrationViewAPI, logout_view, ProtectedView


urlpatterns = [
    re_path('user/login/', AuthorizationViewAPI.as_view()),
    re_path('user/signup/', RegistrationViewAPI.as_view()),
    re_path('user/logout/', logout_view),    
    re_path('user/login-check/', ProtectedView.as_view(), name='login-check'),
]
