from django.urls import path
from . import views

urlpatterns = [
    path('liste/', views.liste_teste, name='liste_teste'),
]
