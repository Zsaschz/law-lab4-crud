from dataclasses import field
from tkinter.messagebox import NO
from rest_framework.serializers import Serializer, FileField, ModelSerializer
from .models import *

# Serializers define the API representation.
class UploadSerializer(ModelSerializer):
    class Meta:
        model = FileUpload
        fields = "__all__"

class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__"