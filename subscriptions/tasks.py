from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from subscriptions.models import Subscriptions


@shared_task
def send_notification(**kwargs):
    """Отправка уведомления о ДР"""
    subscription = Subscriptions.objects.get(pk=kwargs['pk'])
    send_mail(
        subject=f'Оповещение о дне рождении {subscription.birthday_person.first_name} '
                f'{subscription.birthday_person.first_name}',
        message=f'{subscription.birthday_person.birthday} день рождения у {subscription.birthday_person.first_name} '
                f'{subscription.birthday_person.first_name} не забудь поздравить',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[subscription.employees.email]
    )
    subscription.delete()


@shared_task(queue='queue1')
def send_test():
    """Отправка уведомления о ДР"""
    subscription = Subscriptions.objects.get(pk=7)
    print(111)
    subscription.delete()
