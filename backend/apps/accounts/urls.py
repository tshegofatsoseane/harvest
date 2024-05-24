# accounts/urls.py

from django.urls import path
from .views import UserRegistrationAPIView, UserLoginAPIView, UserProfileAPIView

urlpatterns = [
    path('signup/', UserRegistrationAPIView.as_view(), name='user-registration'),
    path('login/', UserLoginAPIView.as_view(), name='user-login'),
    path('profile/', UserProfileAPIView.as_view(), name='user-profile'),
]
