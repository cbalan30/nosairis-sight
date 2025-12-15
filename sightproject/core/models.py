from django.db import models

class UploadedFile(models.Model):
    file = models.FileField(upload_to='csv_uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)
    # Optional: Add fields for processing results or errors
    # status_message = models.CharField(max_length=255, default='Pending')
