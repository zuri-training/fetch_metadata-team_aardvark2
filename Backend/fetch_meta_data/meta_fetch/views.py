from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from meta_fetch.models import ImageData, UserImage,Pdf, UserPdf, JsonData, UserJson, Csv
from rest_framework import generics
from .serializers import ImageDataSerializer, PdfSerializer, JsonDataSerializer, CsvSerializer


#from http.client import HTTPResponse
# Create your views here.

def home(request):
    if request.method == 'GET':
        return HttpResponse("Get Request")
    elif request.method == 'POST':
        return HttpResponse("Post")
    return HttpResponse("Hey, this is meta_fetch")

class ImageDataList(generics.ListCreateAPIView):
    queryset = ImageData.objects.all()
    serializer_class = ImageDataSerializer

class ImageDataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ImageData.objects.all()
    serializer_class = ImageDataSerializer 

class PdfList(generics.ListCreateAPIView):
    queryset = Pdf.objects.all()
    serializer_class = PdfSerializer

class PdfDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pdf.objects.all()
    serializer_class = PdfSerializer 

class JsonDataList(generics.ListCreateAPIView):
    queryset = JsonData.objects.all()
    serializer_class = JsonDataSerializer

class JsonDataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = JsonData.objects.all()
    serializer_class = JsonDataSerializer 

class CsvList(generics.ListCreateAPIView):
    queryset = Csv.objects.all()
    serializer_class = CsvSerializer

class CsvDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Csv.objects.all()
    serializer_class = CsvSerializer 
