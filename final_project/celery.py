import os
from celery import Celery
from datetime import time
from celery.schedules import crontab
#I have no idea what's going on here!

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'final_project.settings')

app = Celery('final_project')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

CELERY_BEAT_SCHEDULE = {
    'up_to_ten': {
        'task': 'companies.tasks.up_to_ten',
        'schedule': crontab(hour=0, minute=0),
    },
}
