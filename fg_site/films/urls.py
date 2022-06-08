from django.urls import path
from .views import *

app_name = 'films'

urlpatterns = [
    path('', premieres_view, name='films'),
    path('<slug:film_slug>/', film_info, name='film_info'),
    # path('<slug:genre_slug>/', filter_genres, name='filter_genres'),
    # path('actor/<str:slug>/', ActorView.as_view(), name="actor_detail"),
]
