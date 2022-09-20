from core.serializers.content import *
from core.models import Content

from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.models import User


class CreateView(CreateAPIView):

    queryset = Content.objects.all()
    serializer_class = CreateSerializer


class RetrieveView(RetrieveAPIView):

    serializer_class = RetrieveSerializer

    def get_queryset(self):
        user = self.request.user
        return user.content_set.all()


class ListView(ListAPIView):

    serializer_class = ListSerializer

    def get_queryset(self):
        user = self.request.user
        return user.content_set.all().values('id', 'title', 'file_format')


class ShareView(APIView):

    def post(self, request):
        serializer = ShareSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_id, content_id = serializer.validated_data['user_id'], serializer.validated_data['content_id']
        try:
            content = Content.objects.get(id=content_id)
        except:
            return Response(
                data={'message': f'Content with id {content_id} does not exist.'},
                status=status.HTTP_404_NOT_FOUND
            )

        try:
            user = User.objects.get(id=user_id)
        except:
            return Response(
                data={'message': f'User with id {user_id} does not exist.'},
                status=status.HTTP_404_NOT_FOUND
            )

        content.users.add(user)

        return Response(data={'message': 'Content shared successfully.'})
