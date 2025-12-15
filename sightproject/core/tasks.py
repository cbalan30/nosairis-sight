from celery import shared_task
import csv
from .models import RawData, UploadedFile
import io
from datetime import datetime

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
                    # Example processing logic  
                unix_timestamp_str = row[6]
                switch_label_str = row[0]

                if unix_timestamp_str and switch_label_str:
                    print(f"Step 1")
                    try:
                        # 2. Convert the string to a float or integer
                        unix_timestamp = float(unix_timestamp_str)
                        print(f"Step 2")

                        if unix_timestamp:
                            print(f"Step 3")
                            # 3. CONVERSION: Use datetime.fromtimestamp()
                            # This function returns a local time datetime object
                            datetime_obj = datetime.fromtimestamp(unix_timestamp)

                            if datetime_obj:
                                print(f"Step 4")
                                # MySQL DATETIME FORMAT
                                formatted_date = datetime_obj.strftime('%Y-%m-%d %H:%M:%S')

                                if formatted_date:
                                    print(f"Step 5")
                                    data = RawData(logtime=formatted_date, switch_label=switch_label_str.strip().upper())
                                    data.t1 = convert_to_boolean(row[1])
                                    data.t2 = convert_to_boolean(row[2])    
                                    data.t3 = convert_to_boolean(row[3])
                                    data.t4 = convert_to_boolean(row[4])
                                    data.t5 = convert_to_boolean(row[5])
                                    data.save()
                                    print(f"Raw data saved: {data}")
                        
                    except ValueError:
                        print(f"Skipping row due to invalid timestamp: {unix_timestamp_str}")
                        # You can choose to skip or assign a default value                
            # ------------------------------------

        uploaded_file.is_processed = True
        uploaded_file.save()
        
    except Exception as e:
        # Handle errors and update status
        print(f"Error processing file {file_id}: {e}")


def convert_to_boolean(value):
    """
    Converts a string or other value to a Python boolean.
    
    Treats common falsy strings (case-insensitive) as False.
    All other values (including 'True', '1', 'Yes', etc.) are treated as True, 
    unless the value is empty or None.
    """
    if value is None:
        return False
        
    if isinstance(value, str):
        # Strip whitespace and convert to lowercase for robust checking
        cleaned_value = value.strip().lower()
        
        # Check for common "falsy" representations
        if cleaned_value in ('false', 'f', '0', 'no', 'n', ''):
            return False
            
    # Default to True for any non-falsy string or any non-zero number
    return bool(value)