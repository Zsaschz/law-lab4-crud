from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.views import *

router = routers.DefaultRouter()
router.register(r'notes', NoteViewSet, basename='note')
router.register(r'file', UploadViewSet, basename='file')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
