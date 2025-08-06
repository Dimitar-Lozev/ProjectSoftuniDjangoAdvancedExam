from django.urls import path
from . import views
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('recipes/<int:pk>/', views.RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipes/create/', views.RecipeCreateView.as_view(), name='recipe_create'),
    path('recipes/<int:pk>/edit/', views.RecipeUpdateView.as_view(), name='recipe_edit'),
    path('recipes/<int:pk>/delete/', views.RecipeDeleteView.as_view(), name='recipe_delete'),
]