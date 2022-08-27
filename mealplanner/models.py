from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Publish Now"))


class Recipes(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_recipes')
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)
    prep_time = models.CharField(max_length=8, default=0)
    cook_time = models.CharField(max_length=8, default=0)
    ingredients = models.TextField(validators=[textfield_not_empty])
    method = models.TextField(validators=[textfield_not_empty])
    dish_image = CloudinaryField('image', default='placeholder')
    bookmarks = models.ManyToMany(User, related_name='bookmark', default=None, blank=True)
    status = models.IntegerField(choice=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str_(self):
        return self.title


class Comments(models.Model):
    recipe = models.ForeignKey(Recipe,on_delete=models.CASCADE, related_name='comment')
    name = models.CharField(max_length=100)
    email = models.Email.Field()
    body = models.TextField()
    commented_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_on']

    def __str_(self):
        return self.body
