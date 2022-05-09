import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'matches.settings')

app = Celery('app')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'matches-collect': {
        'task': 'app.tasks.update_matches',
        'schedule': crontab(minute="*/2"),
    },
}


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')