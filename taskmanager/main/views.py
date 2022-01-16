from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from .forms import TaskForm, Task, RegistrationForm
from django.contrib.auth import logout


def index(request):
    return render(request, 'main/index.html')


def login(request):
    return render(request, 'main/login.html')


def logout_view(request):
    logout(request)
    return redirect('/')


def register(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password1'])
            # Save the User object
            new_user.save()
            return redirect('/')
    else:
        user_form = RegistrationForm()
    return render(request, 'main/registration.html', {'user_form': user_form})


def about(request):
    return render(request, 'main/about.html')

@login_required
def temki(request):
    tasks = Task.objects.all()
    result = render(request, 'main/temki.html', {'titles': 'Главная страница сайта', 'tasks': tasks})
    return result

@login_required
def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('temki')
        else:
            error = 'Темка была не заполнена'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)

