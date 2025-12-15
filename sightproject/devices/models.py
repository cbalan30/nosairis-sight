from django.db import models

class Switch(models.Model):

    switch_id = models.IntegerField(unique=True)
    
    switch_label = models.CharField(max_length=50) 
    
    switch_name = models.CharField(blank=True, max_length=255) 
    
    # This method defines the string representation of an object
    def __str__(self):
        return self.switch_label 

    class Meta:
        # Define default sorting for objects retrieved from the database
        ordering = ['switch_label']

class Terminal(models.Model):

    terminal_id = models.IntegerField(unique=True)
    
    terminal_code = models.CharField(max_length=50) 
    
    terminal_name = models.CharField(blank=True, max_length=255) 
    
    # This method defines the string representation of an object
    def __str__(self):
        return self.terminal_code 

    class Meta:
        # Define default sorting for objects retrieved from the database
        ordering = ['terminal_code']
