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
from .views import ImageDataList, ImageDataDetail, PdfList, PdfDetail, JsonDataList, JsonDataDetail, CsvList, CsvDetail 

urlpatterns = [
   #path('', views.home, name='home'),
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

