from flask import Blueprint, jsonify, request
from controllers.recipe_controller import RecipeController
from models.recipe_model import Recipe

recipe_views = Blueprint('recipe_views', __name__)
controller = RecipeController()

@recipe_views.route('/recipes', methods=['POST'])
def add_recipe():
    data = request.json
    recipe = Recipe(
        title=data['title'],
        author=data['author'],
        type=data['type'],
        description=data['description'],
        video_link=data['video_link'],
        ingredients=data['ingredients'],
        cuisine=data['cuisine']
    )
    controller.add_recipe(recipe)
    return jsonify({"message": "Recipe added successfully"}), 201

@recipe_views.route('/recipes', methods=['GET'])
def get_all_recipes():
    recipes = controller.get_all_recipes()
    return jsonify([recipe.to_dict() for recipe in recipes]), 200

@recipe_views.route('/recipes/<cuisine>', methods=['GET'])
def get_recipes_by_cuisine(cuisine):
    recipes = controller.find_recipes_by_cuisine(cuisine)
    return jsonify([recipe.to_dict() for recipe in recipes]), 200
