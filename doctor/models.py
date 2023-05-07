from django.db import models
from mptt.models import MPTTModel, TreeForeignKey,TreeManyToManyField




class Category(MPTTModel):
    name = models.CharField(max_length=255,unique=True)
    parent = TreeForeignKey("Category",on_delete=models.CASCADE,null=True,blank=True,related_name='children')

    def __str__(self):
        return self.name

# class CustomerCategory(models.Model):
#     name = models.CharField(max_length=255,unique=True)

#     def __str__(self):
#         return f"{self.name}"


# class DoctorCategory(models.Model):
#     name = models.CharField(max_length=255,unique=True)

#     customer_category = models.ForeignKey("CustomerCategory",on_delete=models.SET_NULL,null=True)

#     def __str__(self):
#         return f"{self.name}"
    

class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

class Doctor(models.Model):
    name = models.CharField(max_length=100,unique=True)
    experience = models.PositiveSmallIntegerField()
    doctor_medical_code = models.CharField(max_length=8)
    national_code = models.CharField(max_length=15)
    city = models.ForeignKey("City",on_delete=models.SET_NULL,null=True)
    doctor_category = TreeManyToManyField("Category",related_name="doctors")

    def __str__(self):
        return f"{self.name}"

    