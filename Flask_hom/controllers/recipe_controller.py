from models.recipe_model import Recipe

class RecipeController:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def get_all_recipes(self):
        return self.recipes

    def find_recipes_by_cuisine(self, cuisine):
        return [recipe for recipe in self.recipes if recipe.cuisine == cuisine]
