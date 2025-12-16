# myapp/urls.py

from django.urls import path
from . import views




urlpatterns = [
    path('', views.switch_status, name='switch_status'),
    path('status', views.switch_status, name='switch_status'),

    path('status/chart/', views.SwitchStatusChartView.as_view(), name='switch_status_chart'),
    # URL to fetch the JSON data
    path('status/data/', views.SwitchStatusDataView.as_view(), name='switch_status_data'),

    path('alerts/', views.SwitchAlertsListView.as_view(), name='switch_alerts_list'),
]