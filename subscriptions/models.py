from django.db import models
from django_celery_beat.models import PeriodicTask

from employees.models import Employees
from users.models import User, NULLABLE


class Subscriptions(models.Model):
    birthday_person = models.ForeignKey(Employees, verbose_name='Именинник', on_delete=models.CASCADE)
    employees = models.ForeignKey(User, verbose_name='Сотрудник', on_delete=models.CASCADE)
    notification = models.DateTimeField(verbose_name='Дата/время оповещения')
    task = models.OneToOneField(PeriodicTask, on_delete=models.SET_NULL, verbose_name='Ссылка на периодическую задачу',
                                **NULLABLE)

    def __str__(self):
        return f'{self.pk}:({self.birthday_person} {self.notification})'

    class Meta:
        verbose_name = 'Подписка на ДР'
        verbose_name_plural = 'Подписки на ДР'
