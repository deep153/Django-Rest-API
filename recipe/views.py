from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Recipe,Step,Ingredient
from .serializers import RecipeSerializer
from rest_framework import serializers
from rest_framework import status
from django.http import Http404

# to add & get all recipe 
class RecipeList(APIView):
    def get(self,request):
        recipes = Recipe.objects.all()        
        serializer =  RecipeSerializer(recipes, many='true')
        return Response({"data" : serializer.data}) 

    def post(self, request, format=None):
        recipe = request.data.get('recipe')
        user_id = request.data.get('user_id')
        context = {"user_id" : user_id}

        serializer = RecipeSerializer(data=recipe, context=context)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# to get particular recipe, delete or update recipe
class RecipeDetail(APIView):
    def get_object(self, pk):
        try:
            return Recipe.objects.get(pk=pk)
        except Exception as e:
            error = {'error': 'Invalid recipe id'}
            raise serializers.ValidationError(error)

    def get(self, request, pk, format=None):
        recipe = self.get_object(pk)
        serializer = RecipeSerializer(recipe)
        return Response({"data" : serializer.data})

    def delete(self, request, pk, format=None):
        recipe = self.get_object(pk)
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        recipe = self.get_object(pk)
        recipe_data = request.data.get('recipe')
        user_id = request.data.get('user_id')
        context = {"user_id" : user_id}

        serializer = RecipeSerializer(recipe, data=recipe_data, context=context)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#to get recipe using user id
class UserRecipeView(APIView):

    def get(self, request, uid, format=None):
        recipe = Recipe.objects.filter(user=uid)
        serializer =  RecipeSerializer(recipe, many='true')
        return Response({"data" : serializer.data})


