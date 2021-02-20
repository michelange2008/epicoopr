from django.contrib import admin
from django import forms
from .forms import CommandeForm, PanierForm
from .models.main_models import Unite, Categorie, Product, Commande
from .models.second_models import Panier, Item


class CommandeAdmin(admin.ModelAdmin):

    form = CommandeForm
    list_display = ('name', 'created_at', 'get_products', 'shipping',
                    'closed_at', 'closed', 'delivered_at', 'delivered')
    search_fields = ['name']


class ItemsPanier(admin.TabularInline):

    model = Item
    fieldsets = [
        (None, {'fields': ['product', 'qtt']})
    ]
    extra = 1


@admin.register(Panier)
class PanierAdmin(admin.ModelAdmin):
    inlines = [ItemsPanier]


admin.site.register(Unite)
admin.site.register(Categorie)
admin.site.register(Product)
# admin.site.register(Panier)
admin.site.register(Item)
admin.site.register(Commande, CommandeAdmin)
