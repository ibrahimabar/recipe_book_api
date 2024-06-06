from flask import jsonify, request
from marshmallow import ValidationError
from .service import RecipeService
from .model import Recipe
from .schema import RecipeSchema
from http import HTTPStatus

class RecipeController:
    def __init__(self):
        self.recipe_service = RecipeService()
        self.recipe_schema = RecipeSchema()

    def create_recipe(self, data):
        try:
            validated_data = self.recipe_schema.load(data)
            recipe = Recipe.from_dict(validated_data)
            created_recipe = self.recipe_service.create_recipe(recipe)
            return jsonify(self.recipe_schema.dump(created_recipe)), HTTPStatus.CREATED
        except ValidationError as err:
            return jsonify(err.messages), HTTPStatus.BAD_REQUEST

    def get_all_recipes(self):
        recipes = self.recipe_service.get_all_recipes()
        return jsonify(self.recipe_schema.dump(recipes, many=True)), HTTPStatus.OK

    def get_recipe(self, recipe_id):
        recipe = self.recipe_service.get_recipe(recipe_id)
        if recipe:
            return jsonify(self.recipe_schema.dump(recipe)), HTTPStatus.OK
        else:
            return jsonify({'message': 'Recipe not found'}), HTTPStatus.NOT_FOUND

    def update_recipe(self, recipe_id, data):
        try:
            validated_data = self.recipe_schema.load(data)
            updated_recipe = self.recipe_service.update_recipe(recipe_id, validated_data)
            if updated_recipe:
                return jsonify(self.recipe_schema.dump(updated_recipe)), HTTPStatus.OK
            else:
                return jsonify({'message': 'Recipe not found'}), HTTPStatus.NOT_FOUND
        except ValidationError as err:
            return jsonify(err.messages), HTTPStatus.BAD_REQUEST

    def delete_recipe(self, recipe_id):
        success = self.recipe_service.delete_recipe(recipe_id)
        if success:
            return '', HTTPStatus.NO_CONTENT
        else:
            return jsonify({'message': 'Recipe not found'}), HTTPStatus.NOT_FOUND

    def search_recipes(self, query):
        recipes = self.recipe_service.search_recipes(query)
        return jsonify(self.recipe_schema.dump(recipes, many=True)), HTTPStatus.OK
