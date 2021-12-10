from django.contrib import admin

from .models import Honor


class HonorAdmin(admin.ModelAdmin):
    list_display = ('position', 'rank', 'surname', 'name', 'is_published')
    list_display_links = ('position', 'rank')
    search_fields = ('position', 'rank', 'surname')


admin.site.register(Honor, HonorAdmin)

# Register your models here.
