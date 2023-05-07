from django.contrib import admin
from django.urls import path
from doctor.views import GetDoctorsWithMainCategoryView, GetMainCategorysView

app_name = "doctor_v1"

urlpatterns = [
    # path('first/',FirstApi.as_view(),name="first_api"),
    path('get_main_categorys/',GetMainCategorysView.as_view(),name="get_all_main_categorys"),
    path('doctors/<int:category_id>',GetDoctorsWithMainCategoryView.as_view(),name="get_doctors_with_main_category"),
]

