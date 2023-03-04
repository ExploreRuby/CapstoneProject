from django.test import TestCase
from restaurant import views
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.urls import reverse

class MenuViewTest(TestCase):
    def setup(self):
        Menu.objects.create(title="Rice",price=90,inventory=80)
    def test_getall(self):
        response = self.client.get(reverse('menu'))
        menu_items = Menu.objects.all()
        serialized_items = MenuSerializer(menu_items)
        self.assertEqual(serialized_items,response.data)
