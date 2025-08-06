from django.views import generic
from .models import Recipe, Comment, Rating
from .forms import RecipeForm, CommentForm, RatingForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
class HomeView(generic.ListView):
    model = Recipe
    template_name = 'recipes/home.html'
    context_object_name = 'recipes'
class RecipeDetailView(generic.DetailView):
    model = Recipe
    template_name = 'recipes/recipe_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['rating_form'] = RatingForm()
        return context
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if 'comment' in request.POST:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.author = request.user
                comment.recipe = self.object
                comment.save()
        elif 'rating' in request.POST:
            form = RatingForm(request.POST)
            if form.is_valid():
                Rating.objects.update_or_create(user=request.user, recipe=self.object, defaults={"value": form.cleaned_data['value']})
        return self.get(request, *args, **kwargs)
class RecipeCreateView(LoginRequiredMixin, generic.CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipes/recipe_form.html'
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipes/recipe_form.html'
    success_url = reverse_lazy('home')
    def test_func(self): return self.request.user == self.get_object().author
class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Recipe
    template_name = 'recipes/recipe_confirm_delete.html'
    success_url = reverse_lazy('home')
    def test_func(self): return self.request.user == self.get_object().author
