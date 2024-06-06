from flask import Flask, jsonify, request
from recipes.controller import RecipeController
from config import config

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    recipe_controller = RecipeController()

    @app.route('/recipes', methods=['POST'])
    def create_recipe():
        return recipe_controller.create_recipe(request.json)

    @app.route('/recipes', methods=['GET'])
    def get_all_recipes():
        return recipe_controller.get_all_recipes()

    @app.route('/recipes/<int:recipe_id>', methods=['GET'])
    def get_recipe(recipe_id):
        return recipe_controller.get_recipe(recipe_id)

    @app.route('/recipes/<int:recipe_id>', methods=['PUT'])
    def update_recipe(recipe_id):
        return recipe_controller.update_recipe(recipe_id, request.json)

    @app.route('/recipes/<int:recipe_id>', methods=['DELETE'])
    def delete_recipe(recipe_id):
        return recipe_controller.delete_recipe(recipe_id)

    @app.route('/recipes/search', methods=['GET'])
    def search_recipes():
        query = request.args.get('q', '')
        return recipe_controller.search_recipes(query)

    return app

if __name__ == '__main__':
    app = create_app('development')
    app.run()
