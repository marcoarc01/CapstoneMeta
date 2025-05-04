from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from restaurant.models import MenuTable
from restaurant.serializers import MenuTableSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.token = Token.objects.create(user=self.user)

        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        MenuTable.objects.create(title="Pizza", price=50, inventory=10)
        MenuTable.objects.create(title="Pasta", price=40, inventory=5)

    def test_getall(self):
        response = self.client.get("/menu-items/")
        items = MenuTable.objects.all()
        serializer = MenuTableSerializer(items, many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)
