from django.test import TestCase, Client
from ..models.main_models import Commande
from django.contrib.auth.models import User

# Create your tests here.
class LoginTest(TestCase):

    def setUp(self):
        self.client = Client()

    def tearDown(self):
        self.client.logout()


    def test_routes(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/epicomm/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/epicomm/panier_list')
        self.assertEqual(response.status_code, 301)

    def test_login(self):
        users = User.objects.all()
        for user in users:
            self.client.login(username=user.name)
            response = self.client.get('/epicomm/panier_list')
            self.assertEqual(response.status_code, 301)

    def testRouteCommandeList(self):
        commandes = Commande.objects.all()
        for commande in commandes:
            response = self.client.get(commande.id)
            self.assertEqual(response.status_code, 200)
