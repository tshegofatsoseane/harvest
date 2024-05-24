# accounts/urls.py

from django.urls import path
from .views import UserRegistrationAPIView

urlpatterns = [
    path('signup/', UserRegistrationAPIView.as_view(), name='user-registration'),
]
