from django.urls import path
from django.urls import re_path
from .views import *
from home import views

urlpatterns = [
    path('', index),
    re_path(r'^about', views.about),
    re_path(r'^contacts', views.contacts),
]
