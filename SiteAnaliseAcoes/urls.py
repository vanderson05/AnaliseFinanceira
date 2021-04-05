from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("index/",views.index, name='index'),
]

urlpatterns = [
    path("analise/",views.analise, name='analise'),
]
