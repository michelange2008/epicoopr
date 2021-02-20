from django.db import models
import datetime
from django.utils import timezone
from django.urls import reverse


class Categorie(models.Model):
    """ Catégorie d'aliment: exemple agrûmes, olives et dérivés, café, ..."""

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "catégories de produits"

    name = models.CharField('catégorie', max_length=191, unique=True)
    icon = models.ImageField(upload_to='epicomm', default='default.svg')


class Unite(models.Model):
    """ Unité d'un produit alimentaire avec un nom et une abbreviation """

    def __str__(self):
        return self.name

    name = models.CharField('unité', max_length=191, unique=True)
    abbreviation = models.CharField(
        'unité abbrégée', max_length=191, unique=True)


class Product(models.Model):
    """ Produit alimenaire de base: orange avec sa variété, huile avec sa
    denomination. Définit par un nom, une description, une catégorie
    (cf. class correspondante), une unité (cf. class correspondante),
    """

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = "produit"
        verbose_name_plural = "produits alimentaires"

    name = models.CharField('produit alimentaire', max_length=191, unique=True)
    description = models.TextField('description des produits', blank=True)
    categorie = models.ForeignKey('Categorie', on_delete=models.PROTECT)
    unite = models.ForeignKey('Unite', on_delete=models.PROTECT)
    pu = models.DecimalField(max_digits=8, decimal_places=2)
    packing = models.PositiveIntegerField('conditionnement')
    icon = models.ImageField(default='icone.svg')


class Commande(models.Model):
    """Commande de produits définit par un nom et une liste de Produits
    Cette commmande possèdes des attributs de date (creation, clôture,
    livraison) et d'état (clôturée, livrée)."""

    def __str__(self):
        return f'{self.name} ({self.created_at.strftime("%d/%m/%Y")})'

    def get_absolute_url(self):
        return reverse('commande_detail', args=[str(self.id)])

    """Fonction destinée à l'affichage dans la page admin"""

    def get_products(self):
        return ",".join([str(p) for p in self.products.all()])

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Commande globale"
        verbose_name_plural = "Commandes globales"

    name = models.CharField(
        'nom de la commande',
        max_length=191,
        unique_for_date="created_at"
        )
    products = models.ManyToManyField(Product, verbose_name='produits')
    shipping = models.DecimalField(
        'coût du transport',
        max_digits=8, decimal_places=2,
        default=0)
    created_at = models.DateField('créée le ', default=timezone.now)
    closed_at = models.DateField('fermée le ', blank=True, null=True)
    closed = models.BooleanField('cloturée', default=False)
    delivered_at = models.DateField('livrée le ', blank=True, null=True)
    delivered = models.BooleanField('livrée', default=False)
