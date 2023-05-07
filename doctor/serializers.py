from rest_framework import serializers
from .models import Category,Doctor

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
    

class DockerSerialier(serializers.ModelSerializer):
    city = serializers.StringRelatedField()
    doctor_category = serializers.StringRelatedField(many=True)
    class Meta:
        model = Doctor
        fields = "__all__"



