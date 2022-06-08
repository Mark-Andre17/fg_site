from django.shortcuts import redirect, render
from .models import *
from django.core.paginator import Paginator


def premieres_view(request):
    premieres = Film.objects.order_by('year')[:100]
    genres = Genre.objects.all()
    paginator = Paginator(premieres, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'films/premieres.html', {'page_obj': page_obj, 'genres': genres, 'title': 'Премьеры'})


def film_info(request, film_slug):
    films = Film.objects.get(slug=film_slug)
    context = {'title': 'Фильмы', 'films': films}
    return render(request, 'films/films_info.html', context)


