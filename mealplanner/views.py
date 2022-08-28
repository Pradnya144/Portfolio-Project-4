from django.shortcuts import render
from django.views import generic, View
from .models import Recipes, Comments, MealPlan

class Home(generic.TemplateView):
    template_name = "index.html"

    
class RecipeList(generic.ListView):
    model = Recipes
    queryset = Recipe.objects.filter(ststus=1).order_by('-created_on')
    template_name = 'browse_recipes.html'
    paginate_by = 8



