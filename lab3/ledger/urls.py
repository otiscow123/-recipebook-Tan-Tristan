from django.urls import path
from .views import *

urlpatterns = [
    path("recipe/list", RecipeListView.as_view(), name="recipe_list"),
    path("recipe/<int:pk>", RecipeDetailView.as_view(), name="recipe_detail")
]
app_name = 'ledger'