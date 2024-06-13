from django.db import models

from users.models import NULLABLE, User


class Employees(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=150)
    last_name = models.CharField(verbose_name='Фамилия', max_length=150)
    birthday = models.DateField(verbose_name='Дата рождения')
    email = models.EmailField(verbose_name='Почта', blank=True)
    telegram = models.PositiveBigIntegerField(verbose_name='Телеграмм', **NULLABLE)
    owner = models.OneToOneField(User, verbose_name='Владелец', on_delete=models.SET_NULL, **NULLABLE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
