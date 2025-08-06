from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta: model = User; fields = ["username", "email", "password1", "password2"]
from .models import Profile
class ProfileForm(forms.ModelForm):
    class Meta: model = Profile; fields = ['avatar', 'bio']