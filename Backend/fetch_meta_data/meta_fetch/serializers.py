"""
#create your seralizers here
class SongSerializer(serializers.ModelSerializer):
    artist_id = ArtisteSerializer
    class Meta:
        fields = (
        "id",
        "title",
         "date_released",
         "likes",
         "artist_id"
        )
        model = Song

"""
from rest_framework import serializers
from meta_fetch.models import ImageData, UserImage,Pdf, UserPdf, JsonData, UserJson, Csv

class ImageDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageData

        fields =(
            "id",
            "file_name",
            "created",
            "location",
            "camera_brand_and_model",
            "size",
            "aperture",
            "shutter_speed",
            "iso" ,
            "focal_depth",
            "image_resolution",
            "dot_per_inch",
            "color_profile",

        )

class PdfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pdf

        fields =(
            "id",
            "file_name",
            "file_title",
            "size",
            "author",
            "subject",
            "keywords",
            "producing_aplication",
            "created",
            "modified",
            "hidden_layers",
            "copyright_info",
            "attached_files",

        )



class JsonDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = JsonData

        fields =(
            "id",
            "file_name",
            "modified",
            "size",
            "author",
            "model_id",
            "model_label",
            "model_description",
            "created",
            "model_category",
            "associated_imagefile",
            "associated_thumbnail_imagefile",
            "location",
            "attributes",

        )


class CsvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Csv

        fields =(
            "id",
            "file_name",
            "size",
            "modified",
            "created",
            "field",
            "header",
            "encoding",
        )