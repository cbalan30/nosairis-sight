# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload', views.upload_csv, name='upload'),
    path('upload_success', views.upload_success, name='upload_success'),
]