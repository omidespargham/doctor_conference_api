from django.contrib import admin
from django.urls import path,include

app_name = 'doctor'
urlpatterns = [
    path('v1/',include('doctor.urls_v1',namespace='doctor_v1')),
]

