from django.shortcuts import render, get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from .models import Product, Categorie, Unite, Commande
# Create your views here.


class CommandeView(ListView):
    """Renvoie la liste des commandes"""

    def get_queryset(self):
        return Commande.objects.all()


class CommandeDetailView(DetailView):
    """Renvoie le détail d'une commande"""

    model = Commande

@login_required
def panierSaisie(request, commande_id):
    if request.user.is_authenticated:
        commande = get_object_or_404(Commande, pk=commande_id)
        return render(request, "epicomm/panierSaisie.html", {'commande':commande})
