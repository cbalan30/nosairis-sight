from django.db import models

class UploadedFile(models.Model):
    file = models.FileField(upload_to='csv_uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)
    # Optional: Add fields for processing results or errors
    # status_message = models.CharField(max_length=255, default='Pending')

class RawData(models.Model):
    
    switch_label = models.CharField(max_length=2, null=False)

    t1 = models.BooleanField(default=False)
    t2 = models.BooleanField(default=False)
    t3 = models.BooleanField(default=False)
    t4 = models.BooleanField(default=False)
    t5 = models.BooleanField(default=False)

    logtime = models.DateTimeField(null=True)

    def __str__(self):
        return self.switch_label 

    class Meta:
        # Define default sorting for objects retrieved from the database
        ordering = ['logtime']    
