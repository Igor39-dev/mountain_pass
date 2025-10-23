from django.db import DatabaseError
from django.forms.models import model_to_dict

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

    def partial_update(self, request, *args, **kwargs):
        pereval_obj = self.get_object()
        pereval_data = request.data
        serializer = self.get_serializer(pereval_obj, data=pereval_data, partial=True)

        user_dict = model_to_dict(pereval_obj.user)
        user_dict.pop('id')
        user_data = pereval_data.get('user')

        if pereval_obj.status != "new":
            return Response({"state": 0, 'message': "Можно изменять только перевалы в статусе 'new'"})

        if user_data and user_dict != user_data:
            return Response({"state": 0, 'message': "Нельзя изменять данные пользователя"})

        if serializer.is_valid():
            serializer.save()
        return Response({"state": 1, 'message': 'Перевал успешно обновлен'})
