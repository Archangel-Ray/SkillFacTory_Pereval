from django.shortcuts import render
from rest_framework import viewsets

from Pereval import settings
from .models import (
    Coordinates,
    Level,
    Images,
    SpecificationOfPereval,
)
from .serializers import (
    UserSerializer,
    SpecificationOfPerevalSerializer,
    CoordinatesSerializer,
    LevelSerializer,
    ImagesSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = settings.AUTH_USER_MODEL.objects.all()
    serializer_class = UserSerializer


class CoordinatesViewSet(viewsets.ModelViewSet):
    queryset = Coordinates.objects.all()
    serializer_class = CoordinatesSerializer


class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class ImagesViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer


class SpecificationOfPerevalViewSet(viewsets.ModelViewSet):
    queryset = SpecificationOfPereval.objects.all()
    serializer_class = SpecificationOfPerevalSerializer
