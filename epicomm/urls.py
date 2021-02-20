from django.urls import path
from . import views


urlpatterns = [
    path('', views.CommandeView.as_view(), name='commande_list'),
    path('commande/<int:pk>/', views.CommandeDetailView.as_view(),
         name='commande_detail'),
    path('panier_edit/<int:commande_id>/', views.panier_edit, name="panier_edit"),
    path('panier_list/', views.panier_list, name="panier_list"),
    path('panier_show/<int:panier_id>/', views.panier_show,
         name="panier_show"),
    path('panier_destroy/<int:panier_id>/', views.panier_destroy,
         name="panier_destroy"),
]
