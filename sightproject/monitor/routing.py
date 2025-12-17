from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/chart/', consumers.ChartConsumer.as_asgi()),
]