INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',    
    'core',
    'monitor',
    'devices',
    'reports',
    'switchparser',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nosairis_sight',
        'USER': 'dbuser_wsl',
        'PASSWORD': 'password',
        'HOST': '192.168.192.1',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}



# --- CELERY CONFIGURATION ---
# 1. Message Broker: Where Celery sends and receives messages.
CELERY_BROKER_URL = 'redis://127.0.0.1:6379/0' 

# 2. Result Backend: Where Celery stores task states (success/failure) and results.
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'

# 3. Timezone: Important for scheduling tasks (optional for basic tasks)
CELERY_TIMEZONE = "Asia/Kuala_Lumpur" 

# 4. Optional: Accept only json to enhance security
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']


try:
    # Import the Celery app instance we just configured
    from .celeryapp import app as celeryapp
except ImportError:
    # This handles cases where sightproject.celery_app cannot be imported
    pass


