from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
from django.views.generic.list import *
from .models import Recipe

class recipe_list(ListView):
    template_name = "ledger/recipe_list.html"
    context_object_name = "recipe_container"

    def get_queryset(self):
        return Recipe.objects.all()


class recipe_detail(DetailView):
    template_name = "ledger/recipe_detail.html"
    model = Recipe






