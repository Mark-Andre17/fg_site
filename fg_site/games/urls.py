from django.urls import path
from .views import *
from .views import *

app_name = 'games'

urlpatterns = [
    path('', get_platform, name='games')
]