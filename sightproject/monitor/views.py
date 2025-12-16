from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.db.models import F
from django.views.generic import ListView
from devices.models import Switch, SwitchAlerts, SwitchStatus, SwitchTerminal, Terminal, TerminalStatus
from core.models import RawData
from datetime import datetime, timedelta

# Create your views here.
def switch_status(request):
    return render(request, 'monitor/switch_status.html', {})




class SwitchStatusChartView(View):
    """
    View to render the chart page.
    """
    def get(self, request, *args, **kwargs):
        # You can pass context for the AdminLTE template if needed
        context = {
            'page_title': 'Switch Status Chart',
            # Pass all switches to populate a dropdown/selector if needed
            'switches': Switch.objects.all(),
        }
        return render(request, 'monitor/switch_status.html', context)
    

class SwitchStatusDataViewByRange(View):
    """
    View to provide JSON data for the Chart.js chart, filtered by date range.
    """
    def get(self, request, *args, **kwargs):
        
        # 1. Get query parameters
        user_switch_id = request.GET.get('switch_id')




        # 3. Filter the queryset by the dynamic date range
        queryset = SwitchStatus.objects.select_related('switchobj').filter(switch_id=user_switch_id).order_by('-log_at')

        # --- (The rest of your data structuring logic remains the same) ---
        
        chart_data = {}
        
        for status_log in queryset.iterator():
            switch_name = status_log.switchobj.switch_name if status_log.switchobj else f"ID {status_log.switch_id}"
            
            if switch_name not in chart_data:
                chart_data[switch_name] = {'labels': [], 'data': []}
            
            chart_data[switch_name]['labels'].append(status_log.log_at.strftime('%Y-%m-%d %H:%M:%S'))
            chart_data[switch_name]['data'].append(1 if status_log.status else 0)

        # 4. Format the final output structure
        datasets = []
        for label, data_points in chart_data.items():
            datasets.append({
                'label': label,
                'data': data_points['data'],
            })

        # Get the unique, ordered list of all log_at times for the X-axis
        all_labels = sorted(list(set(
            status.log_at.strftime('%Y-%m-%d %H:%M:%S') 
            for status in queryset
        )))

        data = {
            'labels': all_labels,
            'datasets': datasets,
        }
        
        return JsonResponse(data)


class SwitchStatusDataView(View):
    """
    View to provide JSON data for the Chart.js chart.
    """
    def get(self, request, *args, **kwargs):
        # 1. Get query parameters (e.g., to filter by a specific switch)
        user_switch_id = request.GET.get('switch_id')
        

        queryset = SwitchStatus.objects.select_related('switchobj').filter(switch_id=user_switch_id).order_by('-log_at')[:100]


        # 3. Structure the data for Chart.js
        # Group data by switch_name to support multiple lines on one chart
        chart_data = {}
        
        for status_log in queryset.select_related('switchobj').iterator():
            switch_name = status_log.switchobj.switch_name if status_log.switchobj else f"ID {status_log.switch_id}"
            
            if switch_name not in chart_data:
                chart_data[switch_name] = {
                    'labels': [],  # log_at timestamps
                    'data': [],    # status (0 or 1)
                }
            
            # log_at formatted for display (e.g., 'HH:MM:SS')
            chart_data[switch_name]['labels'].append(status_log.log_at.strftime('%Y-%m-%d %H:%M:%S'))
            
            # Status converted to integer: False -> 0, True -> 1
            chart_data[switch_name]['data'].append(1 if status_log.status else 0)

        # 4. Format the final output structure
        datasets = []
        for label, data_points in chart_data.items():
            # A distinct line/dataset for each switch
            datasets.append({
                'label': label,
                'data': data_points['data'],
                # We'll use the first switch's labels for the x-axis labels
                # (Assuming all switches log at roughly the same times for a shared X-axis)
                'labels': data_points['labels'] 
            })

        # Get the unique, ordered list of all log_at times for the X-axis
        # This is a key step: all datasets share one set of X-axis labels
        all_labels = sorted(list(set(
            status.log_at.strftime('%Y-%m-%d %H:%M:%S') 
            for status in queryset
        )))

        # Final JSON response
        data = {
            'labels': all_labels,
            'datasets': datasets,
        }
        
        return JsonResponse(data)
    


class SwitchAlertsListView(ListView):
    model = SwitchAlerts
    template_name = 'monitor/switch_alerts_datatable.html'
    context_object_name = 'alerts_list'
    paginate_by = 50 # Optional: You can let DataTables handle pagination, but this is good practice

    def get_queryset(self):
        # Use select_related('switchobj') to fetch the related Switch object 
        # in the same database query. This is crucial for performance.
        return SwitchAlerts.objects.select_related('switchobj').all()
    


class RawDataListView(ListView):
    model = RawData
    template_name = 'monitor/raw_data_datatable.html'
    context_object_name = 'data_list'
    paginate_by = 50 

    def get_queryset(self):
        return RawData.objects.all()
    


