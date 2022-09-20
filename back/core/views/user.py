from core.serializers.user import *
from core.models import Content

from rest_framework.views import APIView
from rest_framework import permissions, authentication
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import ListAPIView

from django.contrib.auth import authenticate


class RegisterView(APIView):

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.create(serializer.validated_data)
        token = Token.objects.create(user=user)
        return Response(
            data={'token': token.key},
            status=status.HTTP_200_OK
        )


class LoginView(APIView):

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        serializer = LoginSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        username, password = serializer.data['username'], serializer.data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            token = Token.objects.get(user=user)
            return Response(
                data={'token': token.key},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                data='Username or password is not correct.',
                status=status.HTTP_401_UNAUTHORIZED
            )


class ListView(ListAPIView):

    serializer_class = ListSerializer

    def get_queryset(self):
        content_id = self.kwargs['content_id']
        excluded_ids = Content.objects.get(id=content_id).users.values_list('id', flat=True)
        return User.objects.exclude(id__in=excluded_ids).values('id', 'username')
