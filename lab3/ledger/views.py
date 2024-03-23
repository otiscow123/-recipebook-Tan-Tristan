from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
from django.views.generic.list import *
from .models import Recipe
from django.contrib.auth.mixins import LoginRequiredMixin


class RecipeListView(ListView):
    template_name = "recipe_list.html"
    model = Recipe


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'






