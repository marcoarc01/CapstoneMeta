from django.test import TestCase
from restaurant.models import MenuTable

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuTable.objects.create(title="IceCream", price=80, inventory=100)
        
        self.assertEqual(item.get_item(), "IceCream : 80.00")