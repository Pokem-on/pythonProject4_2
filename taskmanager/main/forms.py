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





class RegistrationForm(forms.ModelForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        widgets ={
            'username': TextInput(attrs={
                'class': 'form-control' 'col-sm-6' 'invalid-feedback',
                'placeholder': 'Username',
            }),
            'first_name': TextInput(attrs={
                'class': 'form-control' 'col-sm-6' 'invalid-feedback',
                'placeholder': 'First Name',
            }),
            'last_name': TextInput(attrs={
                'class': 'form-control' 'col-sm-6' 'invalid-feedback',
                'placeholder': 'Last Name',
            }),
            'email': TextInput(attrs={
                'class': 'form-control' 'col-12' 'invalid-feedback',
                'placeholder': 'email',
            }),

        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Password don\'t match.')
        return cd['password2']



