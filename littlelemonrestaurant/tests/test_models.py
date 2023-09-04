from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(tittle="IceCream", price=80, inventory=100)
        itemstr = item.get_item()

        self.assertEqual(itemstr, "Icecream : 80")  