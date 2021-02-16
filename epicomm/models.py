from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


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
    avaible = models.BooleanField('disponible', default=True)
    packing = models.PositiveIntegerField('conditionnement')
    icon = models.ImageField(default='icone.svg')


class Panier(models.Model):

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Commande individuelle"
        verbose_name_plural = "Commandes individuelles"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ManyToManyField('Item')
    created_at = models.DateField('créée le ', default=timezone.now)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    paid = models.BooleanField('payée')
    collected = models.BooleanField('emmenée')


class Item(models.Model):

    def __str__(self):
        return self.product.name + ' (' + str(self.qtt) + ' ' + self.product.unite.abbreviation + ')'

    class Meta:
        verbose_name = "Produit avec quantité d'un utilisateur"
        verbose_name_plural = "Produits avec quantité d'un utilisateur"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    qtt = models.PositiveIntegerField(null=True)


class Commande(models.Model):

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Commande globale"
        verbose_name_plural = "Commandes globales"

    name = models.CharField('commande', max_length=191, unique=True)
    created_at = models.DateField('créée le ', default = timezone.now)
    closed = models.BooleanField()
    closed_at = models.DateField('fermée le ', blank=True, null=True)
    products = models.ManyToManyField(Product)
