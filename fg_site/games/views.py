from django.shortcuts import render
from .models import *


def get_platform(request):
    platforms = Platform.objects.all()
    return render(request, 'games/games.html', {'platforms': platforms, 'title': 'Игры'})
