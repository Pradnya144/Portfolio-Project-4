from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from .models import Recipes, Comments, MealPlan

class Home(generic.TemplateView):
    template_name = "index.html"


class RecipeList(generic.ListView):
    model = Recipes
    queryset = Recipes.objects.filter(ststus=1).order_by('-created_on')
    template_name = 'browse_recipes.html'
    paginate_by = 8


class RecipeDetail(View):

    def get(self, request, slug):
        
        queryset = Recipes.objects.all()
        recipes = get_object_or_404(queryset, slug=slug)
        comments = recipes.comments.order_by('created_on')
        bookmarked = False
        if recipes.bookmarks.filter(id=self.request.user.id).exists():
            bookmarked = True

        return render(
            request,
            "recipe_detail.html",
            {
                "recipes": recipes,
                "comments": comments,
                "comment_form": CommentForm(),
                "mealplan_form": MealPlanForm(),
                "bookmarked": bookmarked
            },
        )
