from django.db import models


class News(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    comments = models.TextField(blank=True)
    created_at_comments = models.DateTimeField(auto_now_add=True)
    is_published_comments = models.BooleanField(default=True)
    is_published = models.BooleanField(default=True)

