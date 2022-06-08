from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *


app_name = 'films'

router = DefaultRouter()
router.register('films',  FilmsDetailViewSet, basename='films')

urlpatterns = [
    path('', include(router.urls))
]
# urlpatterns = [
#     path('films/', ),
#     path('games/', ),
#     path('actors/', ),
#     path('producers/',),
# ]