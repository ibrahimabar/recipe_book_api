class Recipe:
    def __init__(self, title, description, ingredients, instructions, category, id=None):
        self.id = id
        self.title = title
        self.description = description
        self.ingredients = ingredients
        self.instructions = instructions
        self.category = category

    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data.get('title'),
            description=data.get('description'),
            ingredients=data.get('ingredients'),
            instructions=data.get('instructions'),
            category=data.get('category')
        )

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'ingredients': self.ingredients,
            'instructions': self.instructions,
            'category': self.category
        }

    def update(self, data):
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
