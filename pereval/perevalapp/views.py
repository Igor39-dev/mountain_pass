from django.db import DatabaseError

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from perevalapp.serializers import CoordsSerializer, ImagesSerializer, LevelSerializer, PerevalSerializer, UserSerializer
from perevalapp.models import Coords, Images, Level, Pereval, User

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CoordsViewSet(ModelViewSet):
    queryset = Coords.objects.all()
    serializer_class = CoordsSerializer


class LevelViewSet(ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class ImagesViewSet(ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer


class PerevalViewSet(ModelViewSet):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer
    http_method_names = ['get', 'post', 'patch']
    filterset_fields = ('user__email',)
    

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            if not serializer.is_valid():
                return Response(
                    {"status": 400,
                     "message": serializer.errors,
                     "id": None
                     },
                    status=status.HTTP_400_BAD_REQUEST
                )
            serializer.save()
            return Response(
                { "status": 200,
                  "message": None,
                  "id": serializer.instance.pk },
                status=status.HTTP_200_OK
            )
        except DatabaseError as e:
            return Response(
                {"status": 500,
                 "message": "Ошибка подключения к базе данных",
                 "id": None
                 },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
