from django.db import models


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Найменування')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опублікована')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='Оновлення')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    comments = models.TextField(blank=True, verbose_name='Коментар')
    created_at_comments = models.DateTimeField(auto_now_add=True, verbose_name='Дата коментаря')
    is_published_comments = models.BooleanField(default=True, verbose_name='Опоблікування коментаря')
    is_published = models.BooleanField(default=True, verbose_name='Опоблікування новини')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, blank=True, verbose_name='Категорія')
    comments_user = models.ForeignKey('Comments', on_delete=models.PROTECT, null=True, blank=True,
                                      verbose_name='Коментар')


    def __str__(self):
        return self.title

    """ class Meta вносит изменения в админку:настройка интерфейса, и сортировка
    """
    class Meta:
        verbose_name = 'Новини'
        verbose_name_plural = 'Додати новини'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Найменування категорії')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
        ordering = ['title']


class Comments(models.Model):
    user_id = models.IntegerField()
    news_id = models.IntegerField()
    comments = models.TextField(blank=True, verbose_name='Коментар')
    created_at_comments = models.DateTimeField(auto_now_add=True, verbose_name='Дата коментаря')
    is_published_comments = models.BooleanField(default=True, verbose_name='Опоблікування коментаря')

    def __str__(self):
        return self.comments

    class Meta:
        verbose_name = 'Коментар'
        verbose_name_plural = 'Коментарі'
        ordering = ['-created_at_comments']

