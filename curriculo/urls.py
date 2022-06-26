from django.contrib import admin
from django.urls import path
from .views import CurriculoView

urlpatterns = [
     path('', CurriculoView.as_view(), name='curriculo'),
]