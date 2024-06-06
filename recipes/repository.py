from .model import Recipe

class RecipeRepository:
    def __init__(self):
        self.recipes = {}
        self.next_id = 1

    def create(self, recipe):
        recipe.id = self.next_id
        self.recipes[self.next_id] = recipe
        self.next_id += 1
        return recipe

    def get_all(self):
        return list(self.recipes.values())

    def get_by_id(self, recipe_id):
        return self.recipes.get(recipe_id)

    def update(self, recipe_id, data):
        if recipe_id in self.recipes:
            self.recipes[recipe_id].update(data)
            return self.recipes[recipe_id]
        return None

    def delete(self, recipe_id):
        if recipe_id in self.recipes:
            del self.recipes[recipe_id]
            return True
        return False

    def search(self, query):
        return [recipe for recipe in self.recipes.values() if query.lower() in recipe.title.lower() or query.lower() in recipe.category.lower()]
