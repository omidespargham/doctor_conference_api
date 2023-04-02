from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializer



class FirstApi(APIView):
    def get(self,request):
        return Response({"this is make by avatar !"})
    

class GetCategorys(APIView):
    def get(self,request):
        categorys = Category.objects.all()
        srz_categorys = CategorySerializer(instance=categorys,many=True)
        return Response(data=srz_categorys.data)
