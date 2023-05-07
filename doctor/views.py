from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView,status
from rest_framework.response import Response
from .models import Category, Doctor
from .serializers import CategorySerializer, DockerSerialier

    

class GetMainCategorysView(APIView):
    """
    this Endpoint will give you all the main categorys.

    hint: no parameters needed !
    """
    def get(self,request):
        categorys = Category.objects.filter(parent__isnull=True)
        srz_categorys = CategorySerializer(instance=categorys,many=True)
        return Response(data=srz_categorys.data)


class GetDoctorsWithMainCategoryView(APIView):
    """
    this Endpoint will return you all the doctors due to main_category_id.

    need category_id
    """
    def get(self,request,category_id):
        parent_category = get_object_or_404(Category,id=category_id,parent__isnull=True)
        # doctors = Doctor.objects.filter(doctor_category__id__in=parent_category.get_children())
        doctors = Doctor.objects.filter(doctor_category__id__in=parent_category.get_children()).distinct()
        srz_doctors = DockerSerialier(instance=doctors,many=True)
        return Response(data=srz_doctors.data,status=status.HTTP_200_OK)

