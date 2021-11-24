from django.urls import path
from django.urls import re_path
from .views import *


urlpatterns = [
    path('', index),
    re_path(r'^about/', about),
    re_path(r'^contacts/', contacts),
]
