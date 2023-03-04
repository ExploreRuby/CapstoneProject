from django.test import TestCase
from restaurant import views
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setup(self):
        Menu.objects.create(title="Rice",price=90,inventory=80)
    def test_getall(self):
        menu_items = Menu.objects.all()
        serialized_items = MenuSerializer(menu_items)
        self.assertEqual(serialized_items)
