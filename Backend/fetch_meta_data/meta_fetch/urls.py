"""fetch_meta_data URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
from .views import ImageDataList, ImageDataDetail, PdfList, PdfDetail, JsonDataList, JsonDataDetail, CsvList, CsvDetail 

urlpatterns = [
    path('',  views.index, name='index'),
    path('support/', views.support, name='support'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.loginPage, name='login'),
    path('dashboard1/', views.dashboard1, name='dashboard1'),   
    path('dashboard2/', views.dashboard2, name='dashboard2'),
    path('dashboard3/', views.dashboard3, name='dashboard3'),
    path('dashboard4/', views.dashboard4, name='dashboard4'),
    path('dashboard5/', views.dashboard5, name='dashboard5'),
    path('dashboard6/', views.dashboard6, name='dashboard6'),
    path('faqs/',  views.faqs, name='faqs'),

    path('profile/',  views.profile, name='profile'),
    path('notification/',  views.notification, name='notification'),
    path('account/',  views.account, name='account'),
    path('password/',  views.password, name='password'),
    path('security/',  views.security, name='security'),
    path('document/', views.document, name='document'),

   path("imagedata/", ImageDataList.as_view(), name="imagedata_detail"),
   path("imagedata/<int:imagedata_pk>/", ImageDataDetail.as_view(), name="imagedata_list"),

   path("pdf/", PdfList.as_view(), name="pdf_detail"),
   path("pdf/<int:pdf_pk>/", PdfDetail.as_view(), name="pdf_list"),

   path("jsondata/", JsonDataList.as_view(), name="jsondata_detail"),
   path("jsondata/<int:jsondata_pk>/", JsonDataDetail.as_view(), name="jsondata_list"),

   path("csv/", CsvList.as_view(), name="csv_detail"),
   path("csv/<int:csv_pk>/", CsvDetail.as_view(), name="csv_list"),
   #path('ayo/', views.ayoAgba, name='ayo')
]

