from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from .main_models import Commande, Product


class Panier(models.Model):
    """Panier est une commande d'un utilisateurs en lien avec une Commande.
    Il contient une liste d'items qui sont les produits de la Commande avec une
    quantité. Les autres attributs sont intutifs"""

    def __str__(self):
        return self.commande.name

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Commande individuelle"
        verbose_name_plural = "Commandes individuelles"

    def get_items(self):
        return ",".join([str(i) for i in self.items.all()])

    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             verbose_name='utilisateur')
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE, null=True)
    items = models.ManyToManyField('Product', through='Item')
    created_at = models.DateField('créée le ', default=timezone.now)
    price = models.DecimalField('montant de la commande', max_digits=8,
                                decimal_places=2, default=0)
    paid = models.BooleanField('payée', default=False)
    collected = models.BooleanField('récupérée', default=False)


class Item(models.Model):

    def __str__(self):
        return self.product.name + ' (' + str(self.qtt) + """
         """ + self.product.unite.abbreviation + ')'

    class Meta:
        verbose_name = "Produit avec quantité d'un utilisateur"
        verbose_name_plural = "Produits avec quantité d'un utilisateur"

    panier = models.ForeignKey(Panier, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True,
                                verbose_name='produit')
    qtt = models.PositiveIntegerField(null=True)
