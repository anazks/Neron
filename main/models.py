from django.db import models

# Create your models here.

class Doctor_consultation(models.Model):
    
    Patiant_name = models.CharField(max_length=200)
    Patiant_disease = models.CharField(max_length=200)
    Doctor_name = models.CharField(max_length=200)
    appoiment_time = models.TimeField(auto_now_add=False)
    appointment_date = models.DateField(auto_now_add=False)
    
class DoctorAdd(models.Model):
    
    Doctor_name = models.CharField(max_length=200)
    Doctor_spacial = models.CharField(max_length=200)
    
