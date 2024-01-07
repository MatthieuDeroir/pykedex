from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponseServerError

import requests


def home(request):
  pokemon_list = []

  if 'search' in request.GET:
      search_term = request.GET['search'].lower()
      limit = request.GET['limit'].lower()
      offset = request.GET['offset'].lower()

      api_url_search_partial = f"http://localhost:8000/api/pokemons/pokeapi/get/some/" + search_term + "/" + limit + "/" + offset

      try:
          pokemon_req = requests.get(api_url_search_partial)
          pokemon_list = pokemon_req.json()
      except Exception as e:
          print(f"Error: {e}")
          return HttpResponseServerError("An error occurred while fetching Pokemon data.")

      context = {
          'pokemon_list': pokemon_list,
      }

      return render(request, 'home.html', context)

  return render(request, 'home.html')

def menu(request):
  template = loader.get_template('menu.html')
  return HttpResponse(template.render())

def signup(request):
  template = loader.get_template('signup.html')
  return HttpResponse(template.render())

def signin(request):
  template = loader.get_template('signin.html')
  return HttpResponse(template.render())

