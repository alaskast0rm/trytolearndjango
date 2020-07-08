from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import ListView, DetailView

from .models import Movie


class MoviesView(ListView):
    model = Movie
    queryset = model.objects.all()


class MovieDetailView(DetailView):
    model = Movie
    slug_field = "url"
