from celery import shared_task
import csv
from .models import UploadedFile
import io

@shared_task
def parse_csv_file(file_id):
    try:
        uploaded_file = UploadedFile.objects.get(id=file_id)
        
        # Read the file content
        file_path = uploaded_file.file.path
        
        with open(file_path, 'r') as f:
            reader = csv.reader(f)
            header = next(reader)
            
            # --- Data Parsing Logic Goes Here ---
            for row in reader:
                print(f"Processing row: {row}")
            # ------------------------------------

        uploaded_file.is_processed = True
        uploaded_file.save()
        
    except Exception as e:
        # Handle errors and update status
        print(f"Error processing file {file_id}: {e}")