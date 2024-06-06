from .model import Recipe
from .repository import RecipeRepository

class RecipeService:
    def __init__(self):
        self.recipe_repository = RecipeRepository()

    def create_recipe(self, recipe):
        return self.recipe_repository.create(recipe)

    def get_all_recipes(self):
        return self.recipe_repository.get_all()

    def get_recipe(self, recipe_id):
        return self.recipe_repository.get_by_id(recipe_id)

    def update_recipe(self, recipe_id, data):
        return self.recipe_repository.update(recipe_id, data)

    def delete_recipe(self, recipe_id):
        return self.recipe_repository.delete(recipe_id)

    def search_recipes(self, query):
        return self.recipe_repository.search(query)
