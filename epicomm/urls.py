from django.urls import path
from . import views


urlpatterns = [
    path('', views.CommandeView.as_view(), name='commande_list'),
    path(
        '<int:pk>/',
        views.CommandeDetailView.as_view(),
        name='commande_detail'
        ),
    path('<int:commande_id>/panier', views.panierSaisie, name="panierSaisie")
]
