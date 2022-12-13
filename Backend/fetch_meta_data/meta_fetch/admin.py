from django.contrib import admin
from django.contrib.auth.models import User
from .models import I_mage , UserImage,Pdf, UserPdf, J_son, UserJson, Csv

"""
from .models import user,image

# Register your models here.

"""

#admin.site.register(User)
admin.site.register(I_mage)
admin.site.register(UserImage)
admin.site.register(Pdf)
admin.site.register(UserPdf)
admin.site.register(J_son)
admin.site.register(UserJson)
admin.site.register(Csv)
