from django.contrib import admin
from .models import Recipe, Category, Comment, FavouriteRecipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'category', 'created_on')
    search_fields = ('title', 'description', 'ingredients')
    list_filter = ('category', 'created_on')
    ordering = ('-created_on',)
    readonly_fields = ('created_on', 'updated_on')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'recipe', 'created_on')
    search_fields = ('content', 'author__username')
    list_filter = ('created_on',)

@admin.register(FavouriteRecipe)
class FavouriteRecipeAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe', 'added_on')
    ordering = ('-added_on',)
