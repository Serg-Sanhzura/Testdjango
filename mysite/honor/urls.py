from django.urls import path
from .views import *


urlpatterns = [
    path('honor/', index)
]