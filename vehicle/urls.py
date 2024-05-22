from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index_view),
    path('details/<number_plate>', views.details_view),
]
