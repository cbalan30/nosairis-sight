# This ensures the Celery app is loaded when Django starts.


from .celeryapp import app as celeryapp
__all__ = ('celeryapp',)

import celery
celery.current_app = celeryapp


