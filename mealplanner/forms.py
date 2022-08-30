from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Comments, Recipes, MealPlan

class CommentForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['body'].widget = forms.Textarea(attrs={'rows': 3})

    class Meta:
        
        model = Comments
        fields = ('body',)


class RecipeForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget = forms.Textarea(attrs={'rows': 3})

    class Meta:
        
        model = Recipes
        fields = [
            'title',
            'prep_time',
            'cook_time',
            'method',
            'ingredients',
            'dish_image',
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
        
