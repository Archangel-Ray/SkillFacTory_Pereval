from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from Pereval import settings
from .models import User, SpecificationOfPereval, Coordinates, Level, Images


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


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
        fields = "__all__"


class SpecificationOfPerevalSerializer(WritableNestedModelSerializer):
    """
    Олегу Афанасьеву выписать премию! за drf_writable_nested
    и за то, что он разруливает все косяки СкиллФакТори
    """
    user = UserSerializer()
    coords = CoordinatesSerializer()
    level = LevelSerializer()
    images = ImagesSerializer()

    class Meta:
        model = SpecificationOfPereval
        fields = ['beauty_title', 'title', 'other_titles', 'connect', 'add_time',
                  'user', 'coords', 'status', 'level', 'images']
