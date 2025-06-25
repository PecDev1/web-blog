from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'login__input', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'login__input', 'placeholder': 'Email'}),
            'password1': forms.PasswordInput(attrs={'class': 'login__input', 'placeholder': 'Parol'}),
            'password2': forms.PasswordInput(attrs={'class': 'login__input', 'placeholder': 'Parol'}),
        }


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'login__input', 'placeholder': 'Foydalanuvchi nomlari'}),
            'email': forms.EmailInput(attrs={'class': 'login__input', 'placeholder': 'Email'}),
        }


class CustomLoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'login__input', 'placeholder': 'Foydalanuvchi nomi'}),
            'password': forms.PasswordInput(attrs={'class': 'login__input', 'placeholder': 'Parol'}),
        }
from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=150, required=True, label="Create your username")
    email = forms.EmailField(required=True, label="What's your email?")
    password1 = forms.CharField(widget=forms.PasswordInput(), required=True, label="Create your password")
    password2 = forms.CharField(widget=forms.PasswordInput(), required=True, label="Confirm your password")
