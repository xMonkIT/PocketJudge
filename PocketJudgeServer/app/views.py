from django.shortcuts import render
from django.utils.datetime_safe import datetime

from .models import Contest


def home(request):
    return render(request, 'app/index.html', context={
        'year': datetime.today().year,
        'contests': Contest.objects.filter(parent_contest=None)
    })
