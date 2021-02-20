from django.test import TestCase
from ..models.main_models import Commande


class CommandeTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        commande = Commande.objects.create(
            name='légumes',
            )

    def test_name_label(self):
        commande = Commande.objects.get(pk=1)
        field_label = commande._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'nom de la commande')

    def test_created_at_label(self):
        commande = Commande.objects.get(pk=1)
        field_label = commande._meta.get_field('created_at').verbose_name
        self.assertEqual(field_label, 'créée le ')

    def test_commande_name_avec_date(self):
        commande = Commande.objects.get(pk=1)
        expected_name = f'{commande.name} ({commande.created_at})'
        self.assertEqual(expected_name, str(commande))

    def test_get_absolute_url(self):
        commande = Commande.objects.get(pk=1)
        self.assertEqual(commande.get_absolute_url(), '/epicomm/commande/1/')
