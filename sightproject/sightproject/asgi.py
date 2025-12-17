"""
ASGI config for sightproject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
# Replace 'your_app_name' with the actual name of your app (where routing.py is)
import monitor.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sightproject.settings')

application = ProtocolTypeRouter({
    # Handles traditional HTTP (views, admin, etc.)
    "http": get_asgi_application(),
    
    # Handles WebSocket connections
    "websocket": AuthMiddlewareStack(
        URLRouter(
            monitor.routing.websocket_urlpatterns
        )
    ),
})