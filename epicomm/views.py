from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from .models.main_models import Product, Categorie, Unite, Commande
from .models.second_models import Item, Panier
from .forms import ItemForm
from pprint import pprint
from apps_lib.dump import dd
# Create your views here.


class CommandeView(ListView):
    """Renvoie la liste des commandes"""

    def get_queryset(self):
        return Commande.objects.all()


class CommandeDetailView(DetailView):
    """Renvoie le détail d'une commande"""

    model = Commande

@login_required
def panier_edit(request, commande_id):
    commande = get_object_or_404(Commande, pk=commande_id)
    if request.method == 'POST':
        panier = Panier()
        panier.user = request.user
        panier.commande = commande
        panier.save()
        for product in commande.products.all():

            item = Item()
            item.panier = panier
            item.product = product
            item.qtt = request.POST.get('qtt_' + str(product.id))
            item.save()
        panier.save()
        return redirect('panier_list')
    else:
        return render(
            request,
            "epicomm/panier_edit.html",
            {'commande':commande}
            )

@login_required
def panier_list(request):
    paniers = Panier.objects.filter(user=request.user)
    return render(request, "epicomm/panier_list.html", {'paniers':paniers})

@login_required
def panier_show(request, panier_id):
    panier = Panier.objects.filter(id=panier_id)
    if panier.count() != 0:
        return render(request, "epicomm/panier_show.html", {'panier': panier})
    else:
        return redirect("/epicomm")

@login_required
def panier_destroy(request, panier_id):
    Panier.objects.filter(id=panier_id).delete()
    return redirect('panier_list')
