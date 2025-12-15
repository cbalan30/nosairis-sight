# sightproject/celery_app.py

import os
import sys
import django 
from celery import Celery
from django.conf import settings # Keep this import

# --- Path Fix ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)
# --- End Path Fix ---

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sightproject.settings') 
django.setup() 

app = Celery('sightproject') 

app.config_from_object('django.conf:settings', namespace='CELERY') 
app.autodiscover_tasks()

