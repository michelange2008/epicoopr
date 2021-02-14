from django.db import models


class Product(models.Model):

    """Product est un produit que l'on peut commander et est défini par un nom,
    une description, un prix, une disponibilité et une icone"""

    KILO = 'kg'
    LITRE = 'l'
    UNITE = 'unit'

    UNITES = [
        (KILO, 'kilogrammes'),
        (LITRE, 'litres'),
        (UNITE, 'unité')
    ]

    def __str__(self):

        print(self.name)

    class Meta:

        ordering = ['name']

        verbose_name = "Produit que l'on peut commander"

        verbose_name_plural = "Produits que l'on peut commander"

    name = models.CharField("nom", max_length=191, unique=True)

    description = models.TextField("description", blank=True)

    unite = models.CharField(
        "unité",
        max_length=191,
        choices=UNITES,
        default=KILO)

    conditionnement = models.PositiveIntegerField()
    pu = models.DecimalField(max_digits=8, decimal_places=2)
    dispo = models.BooleanField(default=True)
    icone = models.ImageField(
        upload_to='static/epicomm/icons',
        height_field='h',
        width_field='w')
