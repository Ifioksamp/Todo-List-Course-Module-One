from django import forms
from .models import Profile, Todo
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterFormClass(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')

class TodoFormClass(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'description')

class TodoFormUpdateClass(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'description', 'status')