from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('file_request/',views.file_request),
    path('upload_file/',views.upload_file),
]