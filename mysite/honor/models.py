from django.db import models


class Honor(models.Model):
    position = models.CharField(max_length=150, verbose_name='Посада')
    rank = models.CharField(max_length=50, verbose_name='Звання')
    name = models.CharField(max_length=20, verbose_name='Ім`я')
    surname = models.CharField(max_length=20, verbose_name='Прізвище')
    content = models.TextField(blank=True, verbose_name='Стисла автобіографія')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото співробітника')
    is_published = models.BooleanField(default=True, verbose_name='Опоблікування на дошку')

    def __str__(self):
        return self.surname

    """ class Meta вносит изменения в админку:настройка интерфейса, и сортировка
    """
    class Meta:
        verbose_name = 'Дошка пошани'
        verbose_name_plural = 'Занести на дошку пошани'
        # ordering = ['-created_at']
