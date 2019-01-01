from django.shortcuts import render
from core.models import Movie
from django.views.generic import ListView,DetailView

class MovieList(ListView):
    model=Movie
# Create your views here.
class MovieDetail(DetailView):
    model=Movie