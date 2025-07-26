from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse_lazy
from pyexpat.errors import messages

from .models import Recipe, Comment
from .forms import RecipeForm, CommentForm
from django.core.exceptions import PermissionDenied
class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes/recipe_detail.html'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/recipe_detail.html'
    context_object_name = 'recipes'

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipes/recipe_form.html'
    success_url = reverse_lazy('recipe-list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipes/recipe_form.html'
    success_url = reverse_lazy('recipe-list')

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.created_by

class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recipe
    template_name = 'recipes/recipe_confirm_delete.html'
    success_url = reverse_lazy('recipe-list')

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.created_by

@login_required
def add_comment(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.recipe = recipe
            comment.save()
            return redirect('recipe-detail', pk=pk)
    else:
        form = CommentForm()
    return render(request, 'recipes/add_comment.html', {'form': form})

def form_valid(self, form):
    form.instance.created_by = self.request.user
    messages.success(self.request, 'Recipe created successfully!')
    return super().form_valid(form)