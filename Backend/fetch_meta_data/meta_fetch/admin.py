from django.contrib import admin
from django.contrib.auth.models import User
from .models import ImageData , UserImage,Pdf, UserPdf, JsonData, UserJson, Csv

"""
from .models import user,image

# Register your models here.

"""

#admin.site.register(User)
admin.site.register(ImageData)
admin.site.register(UserImage)
admin.site.register(Pdf)
admin.site.register(UserPdf)
admin.site.register(JsonData)
admin.site.register(UserJson)
admin.site.register(Csv)
