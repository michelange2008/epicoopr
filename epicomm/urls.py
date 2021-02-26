from django.urls import path, include
from .views import commande_views, panier_views


urlpatterns = [

    path('', commande_views.CommandeView.as_view(), name='commande_list'),

    path('commande/<int:pk>/', commande_views.CommandeDetailView.as_view(),
         name='commande_detail'),

    path('paniers/liste/', panier_views.panier_list, name="panier_list"),

    path('panier_create/<int:commande_id>/', panier_views.panier_create,
         name="panier_create"),

    path('panier/<int:panier_id>/', include([
        path('modifier/', panier_views.panier_edit, name="panier_edit"),
        path('voir/', panier_views.panier_show, name="panier_show"),
        path('supprimer/', panier_views.panier_destroy, name="panier_destroy"),
    ])),

]
