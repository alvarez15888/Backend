from django.db import models
from django.utils import timezone

class Lost(models.Model):
    obj = models.CharField(max_length=100, help_text="Enter de object description")
    serial = models.CharField(max_length=100, 
                              blank=True, 
                              null=True, 
                              help_text="Enter the object serial number")
    cell_number = models.CharField(max_length=20,
                                   help_text="Enter a contact number")
    email = models.EmailField(blank=True, null=True, help_text = "Enter a contact email")
    obs = models.TextField(max_length=500, blank=True, null=True, help_text="Enter a description/observation")
    date = models.DateTimeField(default=timezone.now, help_text="Please use the following format: <em>YYYY-MM-DD</em>.")

class Found(models.Model):
    obj = models.CharField(max_length=100, help_text="Enter de object description")
    serial = models.CharField(max_length=100, 
                              blank=True, 
                              null=True, 
                              help_text="Enter the object serial number")
    cell_number = models.CharField(max_length=20,
                                   help_text="Enter a contact number")
    email = models.EmailField(blank=True, null=True, help_text = "Enter a contact email")
    obs = models.TextField(max_length=500, blank=True, null=True, help_text="Enter a description/observation")
    date = models.DateTimeField(default=timezone.now, help_text="Please use the following format: <em>YYYY-MM-DD</em>.")