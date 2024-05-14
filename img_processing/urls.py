from django.urls import path
from . import views

urlpatterns = [
    path('img_processing/',views.img_processing),
]