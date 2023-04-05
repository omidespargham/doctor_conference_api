from rest_framework.serializers import ModelSerializer
from .models import CustomerCategory

class CategorySerializer(ModelSerializer):
    class Meta:
        model = CustomerCategory
        fields = "__all__"
    

