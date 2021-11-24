from django.http import HttpResponse
from django.shortcuts import render
from .models import Honor


def index(request):
    honor = Honor.objects.all()
    context = {
        'honor': honor,
        'title': 'Дошка пошани'
    }
    return render(request, template_name='honor/index.html', context=context)

