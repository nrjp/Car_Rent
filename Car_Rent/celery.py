# Celery settings
import os
from celery import Celery
from django.conf import settings

# app = Celery('booking')

# # Celery configurations
# app.config_from_object('django.conf:settings', namespace='CELERY')

# # Use Redis as the message broker
# app.conf.broker_url = 'redis://localhost:6379/0'

# # Load task modules from all registered Django app configs
# app.autodiscover_tasks()


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Car_Rent.settings")
app = Celery("Car_Rent")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()