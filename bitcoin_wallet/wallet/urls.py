from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login.html', views.login, name='login'),
    path('register.html', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('profile', views.profile, name='profile')
]