from rest_framework import serializers
from .models import Bankbranch

class BankbranchSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Bankbranch
        fields = ('bank_name','image')

