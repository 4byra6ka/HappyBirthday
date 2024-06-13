from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    first_name = models.CharField(verbose_name='Имя', max_length=150)
    last_name = models.CharField(verbose_name='Фамилия', max_length=150)
    email = models.EmailField(verbose_name='Почта')
    register_uuid = models.CharField(max_length=50, **NULLABLE)
    telegram = models.PositiveBigIntegerField(**NULLABLE)
    birthday = models.DateField(verbose_name='Дата рождения')
