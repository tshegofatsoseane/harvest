# views.py in accounts app

from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import UserSerializer, LoginSerializer, TokenPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class SignUpView(generics.CreateAPIView):
    serializer_class = UserSerializer


class LoginView(generics.CreateAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        refresh = RefreshToken.for_user(user)
        data = {
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        }
        return Response(data, status=status.HTTP_200_OK)
