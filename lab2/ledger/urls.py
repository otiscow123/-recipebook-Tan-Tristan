from django.urls import path
from .views import *

urlpatterns = [
    path("recipe/list", recipe_list.as_view(), name="recipe_list"),
    path("recipe/<int:pk>", recipe_detail.as_view(), name="recipe_detail")
]
app_name = 'ledger'