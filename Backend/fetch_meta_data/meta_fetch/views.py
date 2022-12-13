from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from meta_fetch.models import I_mage

#from http.client import HTTPResponse
# Create your views here.

def home(request):
    if request.method == 'GET':
        return HttpResponse("Get Request")
    elif request.method == 'POST':
        return HttpResponse("Post")
    return HttpResponse("Hey, this is meta_fetch")
"""
def register(request):
    if
    r_email = request.get('email')
    r_username =  
    if not User.objects.filter(username=r_username).exists():
        User.objects.create(email=r_email,password=password,last_name=last_name)


from django.http import JsonResponse

def trial(request):
    content={"music":"Drake"}
    return JsonResponse(content)

"""