from django.contrib import admin
from .models import CustomerCategory,City,Doctor,DoctorCategory


admin.site.register(CustomerCategory)
admin.site.register(DoctorCategory)
admin.site.register(Doctor)
admin.site.register(City)



