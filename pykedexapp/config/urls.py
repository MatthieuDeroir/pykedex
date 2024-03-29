"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.views import home
from app.views import menu
from app.views import signup
from app.views import signin
from app.views import pokemon_view
from app.views import pokemon_view2
from app.views import team_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path('/', include('app.urls')),  # Point d'entrée de l'API
    path('api/users/', include('users.urls')),  # Point d'entrée de l'API
    path('api/pokemons/', include('pokemons.urls')),
    path('api/teams/', include('teams.urls')),
    path('home/', home, name='home'),
    path('', menu),
    path('signup', signup),
    path('signin', signin),
    path('pokemon_view', pokemon_view),
    path('pokemon_view2', pokemon_view2),
    path('', include("django.contrib.auth.urls")),
    path('team_view', team_view)

]
