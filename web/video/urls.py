from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('img_processing/', views.img_processing),
    path('img_result/', views.img_result),
    path('about/', views.about),
]