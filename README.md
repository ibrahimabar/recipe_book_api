# Recipe Book API

## Introduction
This is a RESTful API for managing recipes using Flask. It includes endpoints for creating, retrieving, updating, deleting, and searching for recipes.

## Project Structure

recipe_book_api/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── recipes/
│   ├── __init__.py
│   ├── controller.py
│   ├── model.py
│   ├── repository.py
│   ├── service.py
│   ├── schema.py
└── tests/
    ├── __init__.py
    └── test_app.py



## Requirements
- Python 3.8+
- Flask
- Marshmallow

## Installation
1. Clone the repository
    ```sh
    git clone https://github.com/ibrahimabar/recipe_book_api.git
    cd recipe_book_api
    ```

2. Create and activate a virtual environment
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies
    ```sh
    pip install -r requirements.txt
    ```

## Running the Application
1. Set the Flask app environment variable
    ```sh
    export FLASK_APP=app.py
    export FLASK_ENV=development  # Optional, enables debug mode
    ```

2. Run the Flask application
    ```sh
    flask run
    ```

## Testing the Application
To run the unit tests, use the following command:
    ```sh
    python -m unittest discover tests
    ```

## API Endpoints
- `POST /recipes`: Create a new recipe
- `GET /recipes`: Get all recipes
- `GET /recipes/<id>`: Get a recipe by ID
- `PUT /recipes/<id>`: Update a recipe by ID
- `DELETE /recipes/<id>`: Delete a recipe by ID
- `GET /recipes/search?q=<query>`: Search recipes by title or category

## License
This project is licensed under the MIT License.
