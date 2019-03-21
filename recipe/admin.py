from django.contrib import admin
from .models import Recipe
from .models import Step
from .models import Ingredient

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Step)
admin.site.register(Ingredient)
