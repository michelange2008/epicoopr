from django.views.generic import ListView, DetailView
from ..models.main_models import Commande
# Create your views here.


class CommandeView(ListView):
    """Renvoie la liste des commandes"""

    def get_queryset(self):
        return Commande.objects.all()


class CommandeDetailView(DetailView):
    """Renvoie le détail d'une commande"""

    model = Commande
