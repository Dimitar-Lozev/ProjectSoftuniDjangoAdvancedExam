from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Profile
from .forms import RegisterForm, ProfileForm
class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')
class ProfileView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'users/profile.html'
class ProfileEditView(LoginRequiredMixin, generic.UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'users/profile_edit.html'
    success_url = reverse_lazy('profile')
    def get_object(self): return self.request.user.profile