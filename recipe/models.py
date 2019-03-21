from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    name = models.CharField(max_length=500)
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)

class Step(models.Model):
    step_text = models.TextField()
    recipe = models.ForeignKey(Recipe, related_name='steps', on_delete=models.CASCADE)

class Ingredient(models.Model):
    name = models.CharField(max_length=250)
    recipe = models.ForeignKey(Recipe, related_name='ingredients', on_delete=models.CASCADE)

