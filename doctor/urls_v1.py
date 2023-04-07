from django.contrib import admin
from django.urls import path
from doctor.views import FirstApi,GetMainCategorysView

app_name = "doctor_v1"

urlpatterns = [
    path('first/',FirstApi.as_view(),name="first_api"),
    path('get_main_categorys/',GetMainCategorysView.as_view(),name="get_all_main_categorys"),
]

