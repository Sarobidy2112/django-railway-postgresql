from django.shortcuts import render
from .models import Teste

def liste_teste(request):
    personnes = Teste.objects.all()
    return render(request, 'monapp/liste.html', {'personnes': personnes})
