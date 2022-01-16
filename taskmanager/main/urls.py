from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create'),
    path('temki', views.temki, name='temki'),
    path('login', views.LoginView.as_view(), name='login'),
    path('logoutt', views.logout_view, name='logoutt'),
    path('sign-up', views.register, name='sign-up'),





]





