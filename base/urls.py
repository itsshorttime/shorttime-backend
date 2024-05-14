from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('about/', views.about),
    path('img_processing/', views.img_processing),
    path('img_result/', views.img_result),
]