from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(max_length=200)
    fam = models.CharField(max_length=50, verbose_name='Фамилия')
    name = models.CharField(max_length=50, verbose_name='Имя')
    otc = models.CharField(max_length=50, verbose_name='Отчество')
    phone = models.CharField(max_length=16, verbose_name='Телефон')
