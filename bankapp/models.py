from django.db import models

# Create your models here.


class ImageUpload(models.Model):
    name=models.CharField(max_length=49,null=True,blank=True)
    image=models.ImageField(upload_to='images/',null=True,blank=True)

   