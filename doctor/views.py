from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class FirstApi(APIView):
    def get(self,request):
        return Response({"this is make by avatar !"})
