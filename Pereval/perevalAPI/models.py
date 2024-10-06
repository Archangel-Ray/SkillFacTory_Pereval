from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(max_length=200)
    fam = models.CharField(max_length=50, verbose_name='Фамилия')
    name = models.CharField(max_length=50, verbose_name='Имя')
    otc = models.CharField(max_length=50, verbose_name='Отчество')
    phone = models.CharField(max_length=16, verbose_name='Телефон')


class Coordinates(models.Model):
    latitude = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    longitude = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    height = models.IntegerField(null=True)


class Level(models.Model):
    difficulty_1 = 'I'
    difficulty_2 = 'II'
    difficulty_3 = 'III'
    difficulty_4 = 'IV'
    difficulty_5 = 'V'
    difficulty_6 = 'VI'

    LEVEL_CHOICES = {
        (difficulty_1, 'Категория I'),
        (difficulty_2, 'Категория II'),
        (difficulty_3, 'Категория III'),
        (difficulty_4, 'Категория IV'),
        (difficulty_5, 'Категория V'),
        (difficulty_6, 'Категория VI'),
    }

    spring = models.CharField(max_length=3, choices=LEVEL_CHOICES, default=difficulty_1, verbose_name='Весна')
    summer = models.CharField(max_length=3, choices=LEVEL_CHOICES, default=difficulty_1, verbose_name='Лето')
    autumn = models.CharField(max_length=3, choices=LEVEL_CHOICES, default=difficulty_1, verbose_name='Осень')
    winter = models.CharField(max_length=3, choices=LEVEL_CHOICES, default=difficulty_1, verbose_name='Зима')
