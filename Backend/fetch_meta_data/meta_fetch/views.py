from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import Profile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from meta_fetch.models import ImageData, UserImage,Pdf, UserPdf, JsonData, UserJson, Csv
from rest_framework import generics
from .serializers import ImageDataSerializer, PdfSerializer, JsonDataSerializer, CsvSerializer


# Create your views here.

def index(request):
    return render(request, 'index.html')

@login_required(login_url='login')
def support(request):
    return render(request, 'support.html')

@login_required(login_url='login')
def profile(request):
    return render(request, 'profile.html')


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

                #log user in and redirect to account page
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)

                # create profile object for new user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('account') 
        else:
            messages.info(request, 'Password Do Not Match')
            return redirect('signup')
           
    return render(request, 'signup.html')



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('dashboard1')
        else:
           messages.info(request, 'Invalid Credentials') 
           return redirect('login')
    else:
        return render(request, 'login.html')

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard1.html')

@login_required(login_url='login')
def dashboard2(request):
    return render(request, 'dashboard2.html')


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
def settings(request):
    return render(request, 'account.html')


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
