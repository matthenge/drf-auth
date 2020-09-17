from rest_framework import status
from rest_framework.generics import GenericAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from djangoProject1.apps.users.serializers import UserRegistrationSerializer, UserLoginSerializer
from djangoProject1.apps.utils import success_response


class UserRegistrationView(GenericAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        status_code = status.HTTP_201_CREATED
        data = {
            "email": serializer.data.get('email'),
            "username": serializer.data.get("username"),
        }
        return Response(success_response(status_code, data, 'User registered successfully'), status=status_code)


class UserLoginView(RetrieveAPIView):
    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        status_code = status.HTTP_200_OK
        data = {
            "email": serializer.data.get('email'),
            "username": serializer.data.get("username"),
        }
        return Response(success_response(status_code, data, 'User logged in successfully'), status=status_code)
