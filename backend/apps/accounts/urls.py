from django.urls import path
from . import views
from .views import UserSignup

urlpatterns = [
    path('signup/', UserSignup.as_view(), name='user_signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    # Other URL patterns for the accounts app
]