from django.db import models

# Create your models here.


class Bankbranch(models.Model):
    ifsc=models.CharField(max_length=11)
    bank_id=models.CharField(max_length=20)
    branch=models.CharField(max_length=200)
    address=models.CharField(max_length=500)
    city=models.CharField(max_length=50)
    district=models.CharField(max_length=50)
    state=models.CharField(max_length=26)
    bank_name=models.CharField(max_length=49)

    def __str__(self):
        return self.bank_name