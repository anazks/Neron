"""ApnaDoctor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main.views import HomeView, Diabetes, Heart, Breast, consultation, appointment, signup, registration, signout, admin_view, add_doctor, consultation_request, consultation_delete, doctor_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',signup,name='signup'),
    path('registration',registration,name='registration'),
    path('signout',signout,name='signout'),
    path('admin_view',admin_view,name='admin_view'),
    path("home",HomeView,name="home"),
    path("Diabetes",Diabetes,name="diabetes"),
    path("Heart",Heart,name="heart"),
    path("Breast",Breast,name="breast"),
    path('consultation',consultation,name='consultation'),
    path('appointment',appointment,name='appointment'),
    path('add_doctor',add_doctor,name='add_doctor'),
    path('consultation_request',consultation_request,name='consultation_request'),
    path('consultation_delete',consultation_delete,name='consultation_delete'),
    path('doctor_list',doctor_list,name='doctor_list'),
]
