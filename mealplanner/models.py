from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from cloudinary.models import CloudinaryField
from .validators import textfield_not_empty

STATUS = ((0, "Draft"), (1, "Publish Now"))


class Recipe(models.Model):

    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)
    prep_time = models.CharField(max_length=8, default=0)
    cook_time = models.CharField(max_length=8, default=0)
    ingredients = models.TextField(validators=[textfield_not_empty])
    method = models.TextField(validators=[textfield_not_empty])
    image = CloudinaryField('image', default='placeholder')
    bookmarks = models.ManyToManyField(User, related_name='bookmark', default=None, blank=True)
    status = models.IntegerField(choices=STATUS, default=1)

    class Meta:
        ordering = ['-created_on']

    def __str_(self):
        return self.title


class Comment(models.Model):

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comment')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    commented_on = models.DateTimeField(auto_now=True)

    class Meta:

        ordering = ['commented_on']

    def __str_(self):

        return f"Comment {self.body} by {self.name}"


class MealPlan(models.Model):
    
    DAY_CHOICE = [
        (0, "Monday"),
        (1, "Tuesday"),
        (3, "Wednesday"),
        (4, "Thursday"),
        (5, "Friday"),
        (6, "Saturday"),
        (7, "Sunday"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='meal_plan')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='meal_plan_item')
    day = models.IntegerField(choices=DAY_CHOICE, default='0')

    class Meta:
        ordering = ['day']

    def __str__(self):
        return f"Meal Plan for {self.day} by {self.user}"
