from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from .models.main_models import Commande
from .models.second_models import Item, Panier


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('product', 'qtt')


class CommandeForm(forms.ModelForm):

    class Meta:
        model = Commande
        fields = ('name', 'created_at', 'products', 'shipping',
                  'closed_at', 'closed', 'delivered_at', 'delivered')


    def clean(self):
        created_at = self.cleaned_data.get('created_at')
        closed_at = self.cleaned_data.get('closed_at')
        closed = self.cleaned_data.get('closed')
        delivered_at = self.cleaned_data.get('delivered_at')
        delivered = self.cleaned_data.get('delivered')

        if closed_at is not None:
            if closed_at <= created_at:
                raise ValidationError(
                    _("""la date de clôture ne peut être inférieure
                       à la date de création.""")
                )
        else:
            if closed:
                raise ValidationError(
                    _("""on ne peut pas clôturer une commande
                      sans une date de clôture.""")
                )
        if delivered_at is not None:
            if closed_at is None:
                raise ValidationError(
                    _("""La date de livraison ne peut pas être
                      antérieure à la date de commande.""")
                )
            elif not closed:
                raise ValidationError(
                    _("""On ne peut pas avoir une commande livrée,
                       si elle n'a pas été clôturée.""")
                )
        else:
            if delivered:
                raise ValidationError(
                    _("""On ne peut pas avoir une commande livrée,
                      sans date de livraison.""")
                )


class PanierForm(forms.ModelForm):

    class Meta:
        model = Panier
        fields = ['user', 'commande', 'items', 'created_at', 'price',
                  'paid', 'collected']
