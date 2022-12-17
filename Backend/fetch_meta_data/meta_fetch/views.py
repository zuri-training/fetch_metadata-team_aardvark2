from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from meta_fetch.models import ImageData, Pdf, JsonData, Csv
from rest_framework import generics

from .serializers import ImageDataSerializer, PdfSerializer, JsonDataSerializer, CsvSerializer


 #create your views here.


def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                #log user in and redirect to settings page
                user_login = authenticate(username=username, password=password)
                login(request, user_login)
                return redirect('account')


 
        else:
            messages.info(request, 'Password Do Not Match')
            return redirect('signup')
           
    return render(request, 'signup.html')



def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard1')
            
        else:
           messages.info(request, 'Invalid Credentials') 
           return redirect('login')
    else:
        return render(request, 'login.html')


@login_required(login_url='login')
def support(request):
    return render(request, 'support.html')

@login_required(login_url='login')
def profile(request):
    return render(request, 'profile.html')


@login_required(login_url='login')
def dashboard1(request):
    return render(request, 'dashboard1.html')

@login_required(login_url='login')
def dashboard2(request):
    return render(request, 'dashboard2.html')

@login_required(login_url='login')
def dashboard3(request):
    return render(request, 'dashboard3.html')

@login_required(login_url='login')
def dashboard4(request):
    return render(request, 'dashboard4.html')

@login_required(login_url='login')
def dashboard5(request):
    return render(request, 'dashboard5.html')

@login_required(login_url='login')
def dashboard6(request):
    return render(request, 'dashboard6.html')


@login_required(login_url='login')
def password(request):
    return render(request, 'password.html')

@login_required(login_url='login')
def notification(request):
    return render(request, 'notification.html')

@login_required(login_url='login')
def security(request):
    return render(request, 'security.html')

@login_required(login_url='login')
def account(request):
    return render(request, 'account.html')

@login_required(login_url='login')
def document(request):
    return render(request, 'document.html')

@login_required(login_url='login')
def support(request):
    return render(request, 'support.html')

@login_required(login_url='login')
def faqs(request):
    return render(request, 'faqs.html')




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
