from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import View
from .forms import TaskForm, Task, SignUpForm
from django.contrib.auth import logout, authenticate, login



def index(request):
    return render(request, 'main/index.html')


class MyLoginView(View):
    def get(self, request):
        form = MyLoginView
        return render(request, 'main/login.html', {'form': form})

    def post(self, request):
        form = MyLoginView(request, request.POST)
        if form.is_valid():
            username = form.clean_data['username']
            password = form.clean_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return render(request, 'main/login.html', {'form': form})
        else:
            return render(request, 'main/login.html', {'form': form})

""""
class SingUpView(View):
    def  get(self, request):
        form = SignUpForm
        return render(request, 'main/registration.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'main/registration.html', {'form': form})
"""

def logout_view(request):
    logout(request)
    return redirect('/')


def SingUpView(request):
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password1'])
            new_user.save()
            return redirect('/')
    else:
        user_form = SignUpForm()
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
