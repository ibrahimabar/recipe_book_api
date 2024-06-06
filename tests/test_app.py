import unittest
from app import create_app
from http import HTTPStatus

class RecipeTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app().test_client()
        self.app.testing = True

    def test_create_recipe(self):
        response = self.app.post('/recipes', json={
            'title': 'Test Recipe',
            'description': 'Test Description',
            'ingredients': ['Test Ingredient'],
            'instructions': 'Test Instructions',
            'category': 'Test Category'
        })
        self.assertEqual(response.status_code, HTTPStatus.CREATED)

        # Test invalid data
        response = self.app.post('/recipes', json={
            'title': '',
            'description': '',
            'ingredients': [],
            'instructions': '',
            'category': ''
        })
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

    def test_get_all_recipes(self):
        response = self.app.get('/recipes')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_get_recipe(self):
        response = self.app.post('/recipes', json={
            'title': 'Test Recipe',
            'description': 'Test Description',
            'ingredients': ['Test Ingredient'],
            'instructions': 'Test Instructions',
            'category': 'Test Category'
        })
        recipe_id = response.get_json()['id']
        response = self.app.get(f'/recipes/{recipe_id}')
        self.assertEqual(response.status_code, HTTPStatus.OK)

        # Test non-existent recipe
        response = self.app.get('/recipes/999')
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    def test_update_recipe(self):
        response = self.app.post('/recipes', json={
            'title': 'Test Recipe',
            'description': 'Test Description',
            'ingredients': ['Test Ingredient'],
            'instructions': 'Test Instructions',
            'category': 'Test Category'
        })
        recipe_id = response.get_json()['id']
        response = self.app.put(f'/recipes/{recipe_id}', json={
            'title': 'Updated Recipe',
            'description': 'Updated Description',
            'ingredients': ['Updated Ingredient'],
            'instructions': 'Updated Instructions',
            'category': 'Updated Category'
        })
        self.assertEqual(response.status_code, HTTPStatus.OK)

        # Test invalid update data
        response = self.app.put(f'/recipes/{recipe_id}', json={
            'title': '',
            'description': '',
            'ingredients': [],
            'instructions': '',
            'category': ''
        })
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

    def test_delete_recipe(self):
        response = self.app.post('/recipes', json={
            'title': 'Test Recipe',
            'description': 'Test Description',
            'ingredients': ['Test Ingredient'],
            'instructions': 'Test Instructions',
            'category': 'Test Category'
        })
        recipe_id = response.get_json()['id']
        response = self.app.delete(f'/recipes/{recipe_id}')
        self.assertEqual(response.status_code, HTTPStatus.NO_CONTENT)

        # Test deleting non-existent recipe
        response = self.app.delete('/recipes/999')
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    def test_search_recipes(self):
        self.app.post('/recipes', json={
            'title': 'Test Recipe',
            'description': 'Test Description',
            'ingredients': ['Test Ingredient'],
            'instructions': 'Test Instructions',
            'category': 'Test Category'
        })
        response = self.app.get('/recipes/search?q=Test')
        self.assertEqual(response.status_code, HTTPStatus.OK)

        # Test search with no results
        response = self.app.get('/recipes/search?q=NonExistent')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(len(response.get_json()), 0)

if __name__ == '__main__':
    unittest.main()
