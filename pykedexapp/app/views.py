from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from rest_framework import viewsets
import requests


def home(request):
  pokemon_list = []

  if 'search' in request.GET:
    search_term = request.GET['search'].lower()
    limit = request.GET['limit'].lower()
    offset = request.GET['offset'].lower()

      # localhost:8000/api/pokemons/pokeapi/get/some/<str:search_letters>/<int:limit>/<int:offset>
    api_url_search_partial = f"localhost:8000/api/pokemons/pokeapi/get/some/" + search_term + "/" + limit + "/" + offset
    try : 
      pokemon_req = requests.get(api_url_search_partial)
      pokemon_list = pokemon_req.json()
    except :
      print("error")

    context = {
        'pokemon_list': pokemon_list,
    }

    return render(request, 'home.html', context)

def menu(request):
  template = loader.get_template('menu.html')
  return HttpResponse(template.render())

def signup(request):
  template = loader.get_template('signup.html')
  return HttpResponse(template.render())

def signin(request):
  template = loader.get_template('signin.html')
  return HttpResponse(template.render())

