from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from .models import ImageUpload
from .serializers import ImageUploadSerializer
from django.views import View
from rest_framework import status
from rest_framework.views import APIView
from predict import predict
# Create your views here.


class ImageUploadView(APIView):
    def get(self, request,format=None):
            branch = ImageUpload.objects.all()
            serializer = ImageUploadSerializer(branch,many=True)
            return JsonResponse(serializer.data, safe=False)


    def post(self, request, format=None):
        serializer = ImageUploadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            img_path=serializer.data['image'] # (this is image path)
            prob, pred =predict(img_path)
            msg={
            "message":"success",
            "output":prob
            }
            return JsonResponse(msg, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

