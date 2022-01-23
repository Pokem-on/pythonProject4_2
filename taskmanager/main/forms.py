from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from .models import Task
from django.forms import ModelForm, TextInput, Textarea
from django.contrib.auth.models import User
from django import forms


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Го темку!'
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Излогай!'

            }),
        }


class MyLoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={
        'autofocus': True,
        'class': 'form-control'
    }))
    password = forms.CharField(label="Password", strip=False, widget=forms.PasswordInput(attrs={
            'autocomplete': 'current-password',
            'class': 'form-control'
        }),
    )


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))
    password2 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = User
        fields = {'username', 'email'}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'})}