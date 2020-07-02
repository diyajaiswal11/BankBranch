from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Bankbranch
from .serializers import BankbranchSerializer
from django.views import View
# Create your views here.


class IFSCView(View):
    def get(self, request, ifsc):
        branch = Bankbranch.objects.filter(ifsc__iexact=ifsc).first()
        serializer = BankbranchSerializer(branch)
        return JsonResponse(serializer.data, safe=False)


class CityBankView(View):
    def get(self, request, city, bankname):
        citybank = Bankbranch.objects.filter(city__iexact=city, bank_name__icontains=bankname)
        serializer = BankbranchSerializer(citybank, many=True)
        return JsonResponse(serializer.data, safe=False)
