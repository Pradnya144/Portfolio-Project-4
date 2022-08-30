from django.contrib import admin
from .models import Recipes, Comments, MealPlan
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Recipes)
class RecipeAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ('title',)
    summernote_fields = ('method',)


@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'recipe', 'commented_on')
    list_filter = ('commented_on',)
    search_fields = ('name', 'email', 'body')


@admin.register(MealPlan)
class MealPlanAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe', 'day')