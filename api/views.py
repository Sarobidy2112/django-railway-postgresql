from rest_framework import generics
from .models import Produit
from .serializers import ProduitSerializer

class ProduitListCreate(generics.ListCreateAPIView):
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer

class ProduitRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer