from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from .models import Recipes, Comments, MealPlan

class Home(generic.TemplateView):
    template_name = "index.html"


class RecipeList(generic.ListView):
    model = Recipes
    queryset = Recipes.objects.filter(status=1).order_by('-created_on')
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

    def post(self, request, slug):
        queryset = Recipes.objects.filter(status=1)
        queryset = Recipes.objects.filter(status=1)
        recipes = get_object_or_404(queryset, slug=slug)
        comments = recipes.comments.order_by('created_on')
        bookmarked = False
        if recipes.bookmarks.filter(id=self.request.user.id).exists():
            bookmarked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.save()
            messages.success(self.request, 'Comment successfully added')
        else:
            comment_form = CommentForm()

        mealplan_form = MealPlanForm(data=request.POST)

        if mealplan_form.is_valid():
            queryset = MealPlan.objects.filter(
                user=request.user,day=request.POST['day']
            )
            mealplan_item = queryset.first()

            if mealplan_item:
                mealplan_item.recipe = recipes
                messages.success(self.request, 'MealPlan successfully updated')
            else:
                mealplan_item = mealplan_form.save(commit=False)
                mealplan_item.user = request.user
                mealplan_item.recipe = recipe
                messages.success(self.request, 'Recipe added to mealplan')

                mealplan_item.save()

        else:
            mealplan_form = MealPlanForm()

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "comment_form": CommentForm(),
                "mealplan_form": MealPlanForm(),
                "bookmarked": bookmarked
            },
        )
