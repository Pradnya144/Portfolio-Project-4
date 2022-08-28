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