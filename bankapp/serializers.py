from rest_framework import serializers
from .models import Bankbranch

class BankbranchSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Bankbranch
        fields = ('ifsc','bank_id','branch','address','city','district','state','bank_name')

