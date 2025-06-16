from django.urls import path
from .views import ProduitListCreate, ProduitRetrieveUpdateDestroy

urlpatterns = [
    path('produits/', ProduitListCreate.as_view(), name='produit-list-create'),
    path('produits/<int:pk>/', ProduitRetrieveUpdateDestroy.as_view(), name='produit-retrieve-update-destroy'),
]