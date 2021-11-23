from django.db import models


class Honor(models.Model):
    position = models.CharField(max_length=150)
    rank = models.CharField(max_length=50)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)

