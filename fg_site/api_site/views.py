from django.shortcuts import render
from rest_framework import viewsets
from films.models import *

from .serializers import *


class FilmsDetailViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmDetailSerializer
