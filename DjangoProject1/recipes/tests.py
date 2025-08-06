from django.contrib.auth.models import User
from django.test import TestCase

from recipes.models import Category, Recipe


class RecipeModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='pass')
        self.category = Category.objects.create(name='Dessert')
        self.recipe = Recipe.objects.create(title='Test Recipe', description='Just a test', category=self.category, author=self.user)
    def test_recipe_str(self): self.assertEqual(str(self.recipe), 'Test Recipe')
    def test_category_str(self): self.assertEqual(str(self.category), 'Dessert')