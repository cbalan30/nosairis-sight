from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.db.models import F

from devices.models import Switch, SwitchAlerts, SwitchStatus, SwitchTerminal, Terminal, TerminalStatus
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
        # We expect dates in 'YYYY-MM-DD HH:mm:ss' format
        start_date_str = request.GET.get('start_date')
        end_date_str = request.GET.get('end_date')

        # 2. Set default date range (e.g., last 24 hours if dates are missing)
        end_dt = datetime.now()
        start_dt = end_dt - timedelta(hours=24) # Default

        try:
            if start_date_str and end_date_str:
                # Parse the strings into datetime objects
                # dateutil.parser is robust for various formats
                start_dt = parser.parse(start_date_str)
                end_dt = parser.parse(end_date_str)
        except Exception as e:
            # Handle parsing errors, fall back to default range
            print(f"Date parsing error: {e}. Using default range.")


        # 3. Filter the queryset by the dynamic date range
        queryset = SwitchStatus.objects.select_related('switchobj').filter(
            log_at__gte=start_dt,
            log_at__lte=end_dt
        ).order_by('log_at')

        # --- (The rest of your data structuring logic remains the same) ---
        
        chart_data = {}
        
        for status_log in queryset.iterator():
            switch_label = status_log.switchobj.switch_label if status_log.switchobj else f"ID {status_log.switch_id}"
            
            if switch_label not in chart_data:
                chart_data[switch_label] = {'labels': [], 'data': []}
            
            chart_data[switch_label]['labels'].append(status_log.log_at.strftime('%Y-%m-%d %H:%M:%S'))
            chart_data[switch_label]['data'].append(1 if status_log.status else 0)

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
        switch_id = request.GET.get('switch_id')
        
        # 2. Get the latest data (e.g., for the last 24 hours)
        time_limit = datetime.now() - timedelta(hours=24)
        
        # Start with all status logs, filtered by time
        # queryset = SwitchStatus.objects.filter(log_at__gte=time_limit).order_by('log_at')

        queryset = SwitchStatus.objects.select_related('switchobj').filter(
            log_at__gte='2019-11-27 18:00:00',
            log_at__lte='2019-11-27 18:05:00'
        ).order_by('log_at')
        
        if switch_id:
            try:
                # Filter by the requested switch if a valid ID is provided
                queryset = queryset.filter(switch_id=int(switch_id))
            except ValueError:
                # Handle invalid ID gracefully
                pass

        # 3. Structure the data for Chart.js
        # Group data by switch_label to support multiple lines on one chart
        chart_data = {}
        
        for status_log in queryset.select_related('switchobj').iterator():
            switch_label = status_log.switchobj.switch_label if status_log.switchobj else f"ID {status_log.switch_id}"
            
            if switch_label not in chart_data:
                chart_data[switch_label] = {
                    'labels': [],  # log_at timestamps
                    'data': [],    # status (0 or 1)
                }
            
            # log_at formatted for display (e.g., 'HH:MM:SS')
            chart_data[switch_label]['labels'].append(status_log.log_at.strftime('%Y-%m-%d %H:%M:%S'))
            
            # Status converted to integer: False -> 0, True -> 1
            chart_data[switch_label]['data'].append(1 if status_log.status else 0)

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