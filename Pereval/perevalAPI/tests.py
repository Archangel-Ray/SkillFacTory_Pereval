from django.urls import reverse
from rest_framework import status

from rest_framework.test import APITestCase

from perevalAPI.models import SpecificationOfPereval, User, Coordinates, Level, Images
from perevalAPI.serializers import SpecificationOfPerevalSerializer


class PerevalAPITestCase(APITestCase):
    def setUp(self):
        self.pereval = SpecificationOfPereval.objects.create(
            beauty_title='гора.',
            title='Эльбрус',
            other_titles='Вершина',
            connect='',
            user=User.objects.create(
                email='user1@mail.ru',
                fam='Фамилия',
                name='Имя',
                otc='Отчество',
                phone='+0 000 000-00-00'
            ),
            coords=Coordinates.objects.create(
                latitude='43.348788',
                longitude='42.445124',
                height='5642'
            ),
            level=Level.objects.create(
                winter='V',
                spring='V',
                summer='V',
                autumn='V'
            ),
        )

        self.image_1 = Images.objects.create(
            data='https://turfirmarus.ru/assets/galleries/233/2.jpg',
            title='Описание',
            pereval=self.pereval
        )

    def test_get_list(self):
        url = f'{reverse("specificationofpereval-list")}?get_all=true'
        response = self.client.get(url)
        serializer_data = SpecificationOfPerevalSerializer(self.pereval).data
        self.assertEqual(serializer_data, response.data)
        self.assertEqual(len(serializer_data), 2)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
