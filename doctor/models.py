from django.db import models



class CustomerCategory(models.Model):
    name = models.CharField(max_length=255,unique=True)

    def __str__(self):
        return f"{self.name}"


class DoctorCategory(models.Model):
    name = models.CharField(max_length=255,unique=True)
    parent = models.ForeignKey("DoctorCategory",on_delete=models.CASCADE,null=True,blank=True)
    customer_category = models.ForeignKey("CustomerCategory",on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return f"{self.name}"
    

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
    doctor_category = models.ManyToManyField("DoctorCategory")

    def __str__(self):
        return f"{self.name}"

    