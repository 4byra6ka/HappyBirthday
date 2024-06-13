import json
from django_celery_beat.models import PeriodicTask, CrontabSchedule


def create_periodic_task(pk, time):
    """Создание периодической задачи"""
    schedule_datatime, _ = CrontabSchedule.objects.get_or_create(minute=time.minute, hour=time.hour,
                                                                 day_of_month=time.day, month_of_year=time.month)
    return PeriodicTask.objects.create(
        crontab=schedule_datatime,
        name=f'{pk}',
        task='subscriptions.tasks.send_notification',
        args=json.dumps({}),
        kwargs=json.dumps({'pk': pk})
    )
