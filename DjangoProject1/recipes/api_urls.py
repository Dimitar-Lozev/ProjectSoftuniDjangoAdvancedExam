from rest_framework.routers import DefaultRouter

from recipes.rest_api import RecipeViewSet

router = DefaultRouter()
router.register(r'recipes', RecipeViewSet)
urlpatterns = router.urls