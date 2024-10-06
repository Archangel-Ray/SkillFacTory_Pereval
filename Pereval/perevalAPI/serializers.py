from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from Pereval import settings
from .models import SpecificationOfPereval, Coordinates, Level, Images


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = settings.AUTH_USER_MODEL
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
    class Meta:
        model = SpecificationOfPereval
        fields = "__all__"
