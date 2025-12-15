from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'core/main_dashboard.html', {})
    # return render(request, 'adminlte/login.html', {})
