from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Comment, Recipe, MealPlan


class CommentForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['body'].widget = forms.Textarea(attrs={'rows': 3})

    class Meta:
        
        model = Comment
        fields = ('body',)


class RecipeForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        
    class Meta:
        
        model = Recipe
        fields = [
            'title',
            'prep_time',
            'cook_time',
            'method',
            'ingredients',
            'image',
            'status',
        ]
        widgets = {
            'method': SummernoteWidget(),
            'ingredients': SummernoteWidget(),
        }


class MealPlanForm(forms.ModelForm):
    
    class Meta:
        
        model = MealPlan
        fields = ('day',)
        
