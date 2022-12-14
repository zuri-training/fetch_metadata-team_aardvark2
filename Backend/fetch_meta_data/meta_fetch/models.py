from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length = 50)
    email = models.EmailField()
    password = models.CharField(max_length=50,  blank=False, null=False, default = "password")


class ImageData(models.Model):
    #user_id = models.ForeignKey("user", on_delete = models.CASCADE)
    id = models.IntegerField(primary_key=True)
    file_name = models.CharField(max_length=50, blank=True, null=True)
    created = models.DateField(auto_now=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    camera_brand_and_model = models.CharField(max_length=50,default = 0) 
    size = models.IntegerField()
    aperture = models.CharField(max_length=50, blank=True, null=True)
    shutter_speed = models.CharField(max_length=50, blank=True, null=True)
    iso = models.CharField(max_length=50, blank=True, null=True)
    focal_depth = models.CharField(max_length=50, blank=True, null=True)
    image_resolution = models.CharField(max_length=50, blank=True, null=True)
    dot_per_inch = models.CharField(max_length=50, blank=True, null=True)
    color_profile = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)

    def __str__(self):
        return self.file_name
    
class UserImage(models.Model):
    user_id = models.ForeignKey("User",on_delete=models.CASCADE)
    image_id = models.ForeignKey("ImageData",on_delete=models.CASCADE)

class Pdf(models.Model):
    id = models.IntegerField(primary_key=True)
    file_name = models.CharField(max_length=50, blank=True, null=True)
    file_title = models.CharField(max_length=50, blank=True, null=True)
    size = models.CharField(max_length=50, blank=True, null=True)
    author = models.CharField(max_length=50, blank=True, null=True)
    subject = models.CharField(max_length=50, blank=True, null=True)
    keywords = models.CharField(max_length=50, blank=True, null=True)
    producing_aplication = models.CharField(max_length=50, blank=True, null=True)
    created = models.DateField(auto_now=True)
    modified = models.DateField(auto_now=True)
    hidden_layers = models.IntegerField()
    copyright_info = models.IntegerField()
    attached_files = models.FileField(upload_to='')

    def __str__(self):
        return self.file_name 
   
class UserPdf(models.Model):
    user_id = models.ForeignKey("User",on_delete=models.CASCADE)
    pdf_id = models.ForeignKey("Pdf",on_delete=models.CASCADE)

class JsonData(models.Model):
    id = models.IntegerField(primary_key=True)
    file_name = models.CharField(max_length=50, blank=True, null=True)
    size = models.CharField(max_length=50, blank=True, null=True)
    author = models.CharField(max_length=50, blank=True, null=True)
    created = models.DateField(auto_now=True)
    modified = models.DateField(auto_now=True)
    model_id = models.IntegerField()
    model_label = models.CharField(max_length=50, blank=True, null=True)
    model_description = models.CharField(max_length=50, blank=True, null=True)
    model_category = models.CharField(max_length=50, blank=True, null=True)
    associated_imagefile = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    associated_thumbnail_imagefile =  models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    location =  models.CharField(max_length=50, blank=True, null=True)
    attributes =  models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.file_name

class UserJson(models.Model):
    user_id = models.ForeignKey("User",on_delete=models.CASCADE)
    json_id = models.ForeignKey("JsonData",on_delete=models.CASCADE)

class Csv(models.Model):
    id = models.IntegerField(primary_key=True)
    file_name = models.CharField(max_length=50, blank=True, null=True)
    size = models.CharField(max_length=50, blank=True, null=True)
    created = models.DateField(auto_now=True)
    modified = models.DateField(auto_now=True)
    field = models.CharField(max_length=50, blank=True, null=True)
    header =  models.CharField(max_length=50, blank=True, null=True)
    encoding = models.BinaryField(max_length=None)

    def __str__(self):
        return self.file_name




    







