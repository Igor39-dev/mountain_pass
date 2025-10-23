from django.test import TestCase

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from perevalapp.serializers import PerevalSerializer
from perevalapp.models import Coords, Images, Level, Pereval, User

class PerevalTestCase(APITestCase):
    def setUp(self):

# 1ый объект
        self.pereval_1 = Pereval.objects.create(
            beauty_title='beauty_title1',
            title='title_1',
            other_titles='other_titles1',
            connect='connect1',
            add_time='2021-09-22T13:18:00Z',
            user=User.objects.create(
                email='email1@email.ru',
                fam='fam_1',
                name='name_1',
                otc='otc_1',
                phone='+7 000 00 01',
            ),
            coords=Coords.objects.create(
                latitude=123.00,
                longitude=456.00,
                height=1000
            ),
            level=Level.objects.create(
                winter='1A',
                summer='1A',
                autumn='1A',
                spring='',
            ),
        )


        self.image_1_1 = Images.objects.create(
            title='title_image_1_1',
            data='data_image_1_1',
            pereval=self.pereval_1
        )

        self.image_1_1 = Images.objects.create(
            title='title_image_1_2',
            data='data_image_1_2',
            pereval=self.pereval_1
        )

# 2ой объект
        self.pereval_2 = Pereval.objects.create(
            beauty_title='beauty_title2',
            title='title_2',
            other_titles='other_titles2',
            connect='connect1',
            add_time='2021-09-22T13:18:00Z',
            user=User.objects.create(
                email='email2@email.ru',
                fam='fam_2',
                name='name_2',
                otc='otc_2',
                phone='+7 000 00 01',
            ),
            coords=Coords.objects.create(
                latitude=123.02,
                longitude=456.02,
                height=1002
            ),
            level=Level.objects.create(
                winter='1B',
                summer='1B',
                autumn='1B',
                spring='1C',
            ),
        )


        self.image_2_1 = Images.objects.create(
            title='title_image_2_1',
            data='data_image_2_1',
            pereval=self.pereval_2
        )

        self.image_2_1 = Images.objects.create(
            title='title_image_2_2',
            data='data_image_2_2',
            pereval=self.pereval_2
        )


    def test_get_list(self):
        url = reverse('pereval-list')
        response = self.client.get(url)
        serializer_data = PerevalSerializer([self.pereval_1, self.pereval_2], many=True).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer_data)
        self.assertEqual(2, len(serializer_data))


    def test_get_detail(self):
        url = reverse('pereval-detail', kwargs={'pk': self.pereval_1.pk})
        response = self.client.get(url)
        serializer_data = PerevalSerializer(self.pereval_1).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer_data)
        