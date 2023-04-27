from pyexpat import model
from django.contrib import admin
from .models import Doctor_consultation,DoctorAdd

# Register your models here.
admin.site.register(Doctor_consultation)
admin.site.register(DoctorAdd)
