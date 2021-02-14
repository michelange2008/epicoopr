from django.db import models


class Categorie(models.Model):

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "catégories de produits"

    name = models.CharField('catégorie', max_length=191, unique=True)
    icon = models.ImageField(upload_to='epicomm')


class Unite(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField('unité', max_length=191, unique=True)
    abbreviation = models.CharField(
        'unité abbrégée', max_length=191, unique=True)


class Product(models.Model):

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
