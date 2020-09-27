from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from .models import Bankbranch
from .serializers import BankbranchSerializer
from django.views import View
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.


class IFSCView(APIView):
    def get(self, request,format=None):
            branch = Bankbranch.objects.all()[:5]
            serializer = BankbranchSerializer(branch,many=True)
            return JsonResponse(serializer.data, safe=False)


    def post(self, request, format=None):
        serializer = BankbranchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CityBankView(View):
    def get(self, request, city, bankname):
        citybank = Bankbranch.objects.filter(city__iexact=city, bank_name__icontains=bankname)
        serializer = BankbranchSerializer(citybank, many=True)
        return JsonResponse(serializer.data, safe=False)


    

