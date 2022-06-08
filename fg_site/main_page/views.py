from django.shortcuts import render
from .utils import menu


def home_view(request):
    return render(request, 'main_page/home_view.html', {'menu': menu})
