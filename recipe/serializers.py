from rest_framework import serializers
from .models import Recipe,Step,Ingredient
from django.contrib.auth.models import User

class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = ("step_text",)

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ("name",) 

class RecipeSerializer(serializers.ModelSerializer):

    steps = StepSerializer(many=True)
    ingredients = IngredientSerializer(many=True) 
    user = serializers.PrimaryKeyRelatedField(read_only=True) #no need to insert new user in every request

    class Meta:
        model = Recipe
        fields = ("id", "name", "steps", "ingredients", "user")  

    #add recipe
    def create(self, validated_data):
        step_data = validated_data.pop('steps')
        ingredients_data = validated_data.pop('ingredients')
        user_id = self.context["user_id"]
        
        try:
            user = User.objects.get(pk=user_id)
        except Exception as e:
            error = {'error': 'User id not found'}
            raise serializers.ValidationError(error)

        recipe = Recipe.objects.create(user=user, **validated_data)

        #insert steps data
        for step_data in step_data:
            Step.objects.create(recipe=recipe, **step_data)
        
        #insert ingredients data
        for ingredients_data in ingredients_data:
            Ingredient.objects.create(recipe=recipe, **ingredients_data)

        return recipe

    #edit recipe
    def update(self, instance, validated_data):
        step_data = validated_data.pop('steps')
        ingredients_data = validated_data.pop('ingredients')
        user_id = self.context["user_id"]

        try:
            user = User.objects.get(pk=user_id)
        except Exception as e:
            error = {'error': 'Invalid User id'}
            raise serializers.ValidationError(error)

        Step.objects.filter(recipe=instance.id).delete()
        Ingredient.objects.filter(recipe=instance.id).delete()

        #insert steps data
        for step_data in step_data:
            Step.objects.create(recipe=instance, **step_data)

        #insert ingredients data
        for ingredients_data in ingredients_data:
            Ingredient.objects.create(recipe=instance, **ingredients_data)    

        instance.name = validated_data.get('name', instance.name)
        instance.user = user
        instance.save()

        return instance



    