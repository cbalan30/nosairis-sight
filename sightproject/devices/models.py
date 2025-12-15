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


class SwitchTerminal(models.Model):

    switch_id = models.IntegerField()
    terminal_id = models.IntegerField()
           
    # This method defines the string representation of an object
    def __str__(self):
        return str(self.switch_id) + " - " + str(self.terminal_id)

    class Meta:
        unique_together = (('switch_id', 'terminal_id'),)
        ordering = ['switch_id',  'terminal_id']        



class SwitchStatus(models.Model):

    switch_id = models.IntegerField(null=False)
    log_at = models.DateTimeField(null=False)
    status = models.BooleanField(default=False)

           
    # This method defines the string representation of an object
    def __str__(self):
        return str(self.switch_id) + " - " + str(self.log_at)

    class Meta:
        unique_together = (('switch_id', 'log_at'),)
        ordering = ['log_at',  'switch_id']


class TerminalStatus(models.Model):

    switch_terminal_id = models.IntegerField(null=False)
    log_at = models.DateTimeField(null=False)
    status = models.BooleanField(default=False)

           
    # This method defines the string representation of an object
    def __str__(self):
        return str(self.switch_terminal_id) + " - " + str(self.log_at)

    class Meta:
        unique_together = (('switch_terminal_id', 'log_at'),)
        ordering = ['log_at',  'switch_terminal_id']           
