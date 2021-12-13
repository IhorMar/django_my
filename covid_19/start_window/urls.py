
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('asia', views.asia, name='asia'),
    path('europe', views.europe, name='europe'),
    path('ukraine', views.ukraine, name='ukraine'),
]