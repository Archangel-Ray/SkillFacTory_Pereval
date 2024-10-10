from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from Pereval import settings
from .models import User, SpecificationOfPereval, Coordinates, Level, Images


class UserSerializer(serializers.ModelSerializer):
    def save(self, **kwargs):
        self.is_valid()
        user = User.objects.filter(email=self.validated_data.get('email'))

        if user.exists():
            return user.first()
        else:
            new_user = User.objects.create(
                username=self.validated_data.get('email'),
                email=self.validated_data.get('email'),
                phone=self.validated_data.get('phone'),
                fam=self.validated_data.get('fam'),
                name=self.validated_data.get('name'),
                otc=self.validated_data.get('otc'),
            )
            return new_user

    class Meta:
        model = User
        fields = ['email', 'fam', 'name', 'otc', 'phone']


class CoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinates
        fields = "__all__"


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = "__all__"


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ['data', 'title']


class SpecificationOfPerevalSerializer(WritableNestedModelSerializer):
    """
    Олегу Афанасьеву выписать премию! за drf_writable_nested
    и за то, что он разруливает все косяки СкиллФакТори
    """
    user = UserSerializer()
    coords = CoordinatesSerializer()
    level = LevelSerializer()
    images = ImagesSerializer(many=True)

    class Meta:
        model = SpecificationOfPereval
        fields = ['beauty_title', 'title', 'other_titles', 'connect', 'add_time',
                  'user', 'coords', 'status', 'level', 'images']
