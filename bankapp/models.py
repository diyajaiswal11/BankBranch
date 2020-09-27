from django.db import models

# Create your models here.


class Bankbranch(models.Model):
    bank_name=models.CharField(max_length=49)
    image=models.ImageField(upload_to='images/',null=True,blank=True)

    def __str__(self):
        return self.bank_name