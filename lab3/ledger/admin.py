from django.contrib import admin
from .models import Recipe, RecipeIngredient


# Register your models here.

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredientInline,]

    search_fields = ['name',]
    list_display = ['name',]
    list_filter = ['name',]

admin.site.register(Recipe, RecipeAdmin)