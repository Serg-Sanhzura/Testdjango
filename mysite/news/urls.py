from django.urls import path
from .views import *


urlpatterns = [
    path('news/', index, name='news'),
    path('category/<int:category_id>/', get_category, name='category'),
]

