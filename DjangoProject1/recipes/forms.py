from django import forms
from .models import Recipe, Comment, Rating
class RecipeForm(forms.ModelForm):
    class Meta: model = Recipe; fields = ['title', 'description', 'image', 'category']
class CommentForm(forms.ModelForm):
    class Meta: model = Comment; fields = ['content']
class RatingForm(forms.ModelForm):
    class Meta: model = Rating; fields = ['value']