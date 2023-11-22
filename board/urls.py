from django.urls import path
from .views import *
urlpatterns = [
    path('', BoardList , name = 'boardList' ),
]