from django.urls import reverse
from rest_framework import status

from rest_framework.test import APITestCase

from perevalAPI.models import SpecificationOfPereval, User, Coordinates, Level, Images
from perevalAPI.serializers import SpecificationOfPerevalSerializer


class PerevalAPITestCase(APITestCase):
    def setUp(self):
        self.pereval1 = SpecificationOfPereval.objects.create(
            beauty_title='гора.',
            title='Эльбрус',
            other_titles='Вершина',
            connect='',
            user=User.objects.create(
                username='user1',
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
            pereval=self.pereval1
        )

        self.pereval2 = SpecificationOfPereval.objects.create(
            beauty_title='гора.',
            title='Эльбрус',
            other_titles='Седловина',
            connect='',
            user=User.objects.create(
                username='user2',
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
                winter='IV',
                spring='IV',
                summer='VI',
                autumn='VI'
            ),
        )

        self.image_1 = Images.objects.create(
            data='https://cdn.culture.ru/images/beaf2c77-3b60-5c9f-97e6-e850fe5d8ec5',
            title='Красивый вид на Эльбрус',
            pereval=self.pereval2
        )

    def test_get_list(self):
        url = f'{reverse("specificationofpereval-list")}?get_all=true'
        response = self.client.get(url)
        serializer_data = SpecificationOfPerevalSerializer([self.pereval1, self.pereval2], many=True).data
        self.assertEqual(serializer_data, response.data)
        self.assertEqual(len(serializer_data), 2)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
