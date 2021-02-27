from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models.main_models import Commande
from ..models.second_models import Panier, Item


@login_required
def panier_create(request, commande_id):
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
        panier = Panier.objects.filter(commande=commande_id)
        if panier is None:
            return render(request, 'epicomm/panier/panier_edit.html',
                          {'panier': panier})
        else:
            return render(request,
                          "epicomm/panier/panier_create.html",
                          {'commande': commande})


@login_required
def panier_list(request):
    paniers = Panier.objects.filter(user=request.user)
    return render(request, "epicomm/panier/panier_list.html",
                  {'paniers': paniers})


@login_required
def panier_edit(request, panier_id):
    panier = Panier.get(pk=panier_id)
    return render(request, "epicomm/panier/panier_edit.html",
                  {'panier': panier})


@login_required
def panier_show(request, panier_id):
    panier = Panier.objects.get(id=panier_id)
    if panier is not None:
        return render(request, "epicomm/panier/panier_show.html",{'panier': panier})
    else:
        return redirect("/epicomm")


@login_required
def panier_destroy(request, panier_id):
    Panier.objects.filter(id=panier_id).delete()
    return redirect('panier_list')
