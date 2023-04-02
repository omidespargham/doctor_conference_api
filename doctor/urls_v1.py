from django.contrib import admin
from django.urls import path
from doctor.views import FirstApi

app_name = "doctor_v1"

urlpatterns = [
    path('first/',FirstApi.as_view(),name="first_api"),
]

