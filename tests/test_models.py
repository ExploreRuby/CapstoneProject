from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        menu_item = Menu.objects.create(title="Plain Rice",price=90,inventory=60)
        self.assertEqual(menu_item,"Plain Rice : 90")
