from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create'),
    path('temki', views.temki, name='temki'),
    path('login', MyLoginView.as_view(), name='login'),
    path('logout', views.logout_view, name='logoutt'),
    path('sign-up', views.SingUpView, name='sign-up'),





]





