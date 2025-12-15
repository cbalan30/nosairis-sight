from django.shortcuts import render, redirect
from .models import UploadedFile
from .tasks import parse_csv_file

# Create your views here.
def home(request):
    return render(request, 'core/main_dashboard.html', {})
    # return render(request, 'adminlte/login.html', {})

def upload_csv(request):
    if request.method == 'POST':
        if 'csv_file' in request.FILES:
            uploaded_file = UploadedFile(file=request.FILES['csv_file'])
            uploaded_file.save()
            
            # --- CRUCIAL STEP ---
            # Instead of processing here, we trigger the server-side watcher/worker
            trigger_file_processing(uploaded_file.id) 

            return redirect('upload_success') # Redirect to a status page
    
    return render(request, 'core/upload.html')

def trigger_file_processing(file_id):
    # This sends the task to the Celery broker immediately
    parse_csv_file.delay(file_id)

def upload_success(request):
    return render(request, 'core/upload_success.html', {})
    # return render(request, 'adminlte/login.html', {})
