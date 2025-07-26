from django import forms
from .models import Recipe, Comment


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients', 'steps', 'image', 'category']
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if 'forbidden' in title.lower():
            raise forms.ValidationError('Inappropriate word in title')
        return title

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
