# Name: Imtiaz Adar
# Project: Login And Register Using Django
# Language: Python
# Phone: 01778767775
# Email: imtiazadarofficial@gmail.com

from django.contrib import admin
from django.urls import path, include
from loginandregistrationapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home_page, name='index'),
    path('login/', views.Login, name='login'),
    path('signup/', views.Signup, name='signup'),
    path('logout/', views.Logout, name='logout'),
]
