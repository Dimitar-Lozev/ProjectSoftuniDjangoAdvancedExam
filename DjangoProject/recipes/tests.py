from http.client import responses

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Recipe, Category

UserModel = get_user_model()
class RecipeTest(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(username='testuser', password='pass123')
        self.category = Category.objects.create(name='Test Category')
        self.recipe = Recipe.objects.create(
            title='Test Recipe',
            description='Description here',
            ingredients='Flour, Eggs',
            steps='Mix and bake',
            created_by=self.user,
            category=self.category,
        )
    def test_recipe_list_view(self):
        response = self.client.get(reverse('recipe-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.recipe.title)

    def test_recipe_detail_view(self):
        response = self.client.get(reverse('recipe-detail', args=[self.recipe.pk,]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.recipe.description)

    def test_recipe_create_redirects_for_anonymous(self):
        response = self.client.post(reverse('recipe-create'))
        self.assertRedirects(response, '/accounts/login/?next=/recipes/create/',)

    def test_logged_user_can_create_recipe(self):
        self.client.login(username='testuser', password='pass123')
        response = self.client.post(reverse('recipe-create'), {
            'title': 'New Recipe',
            'description': 'Yummy',
            'ingredients': 'Stuff',
            'steps': 'Do it',
            'category': self.category.pk,
        })
        self.assertEqual(Recipe.objects.count(), 2)

    def test_only_owner_can_edit(self):
        other = UserModel.objects.create_user(username='other', password='pass123')
        self.client.login(username='other', password='pass123')
        response = self.client.get(reverse('recipe-edit', args=[self.recipe.pk]))
        self.assertEqual(response.status_code, 403)

