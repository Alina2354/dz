class RecipeBook:

    def __init__(self):

        self._recipes = []
        self._last_recipe = None

    def add_recipe(self, recipe_dict):
        if not isinstance(recipe_dict, dict):
            raise TypeError("Recipe must be a dictionary")

        if not all(key in recipe_dict for key in ("name", "ingredients", "time")):
            raise ValueError("Recipe must contain 'name', 'ingredients', and 'time' keys")

        if not isinstance(recipe_dict["name"], str):
            raise TypeError("Recipe name must be a string")
        if not isinstance(recipe_dict["ingredients"], list):
            raise TypeError("Ingredients must be a list")
        if not all(isinstance(ing, str) for ing in recipe_dict["ingredients"]):
            raise TypeError("Each ingredient must be a string")
        if not isinstance(recipe_dict["time"], (int, float)):
            raise TypeError("Time must be a number")
        if recipe_dict["time"] <= 0:
            raise ValueError("Time must be positive")


        self._recipes.append(recipe_dict)
        self._last_recipe = recipe_dict

    def remove_recipe(self, name):
        self._recipes = [recipe for recipe in self._recipes if recipe["name"] != name]
        if self._last_recipe and self._last_recipe["name"] == name:
             self._last_recipe = None

    def find_by_ingredient(self, ingredient):
        return [recipe for recipe in self._recipes if ingredient in recipe["ingredients"]]

    @property
    def recipes_count(self):
        return len(self._recipes)

    @property
    def last_recipe(self):
        return self._last_recipe

    @last_recipe.setter
    def last_recipe(self, recipe_dict):
        if not isinstance(recipe_dict, dict):
            raise TypeError("Recipe must be a dictionary")
        if not all(key in recipe_dict for key in ("name", "ingredients", "time")):
            raise ValueError("Recipe must contain 'name', 'ingredients', and 'time' keys")
        self._last_recipe = recipe_dict


if __name__ == '__main__':
    book = RecipeBook()

    book.add_recipe({"name": "Pasta Carbonara", "ingredients": ["pasta", "eggs", "bacon", "cheese"], "time": 20})
    book.add_recipe({"name": "Chicken Stir-fry", "ingredients": ["chicken", "vegetables", "soy sauce"], "time": 25})
    book.add_recipe({"name": "Omelette", "ingredients": ["eggs", "milk", "cheese"], "time": 10})


    print(f"Number of recipes: {book.recipes_count}")


    print(f"Last recipe: {book.last_recipe}")

    egg_recipes = book.find_by_ingredient("eggs")
    print(f"Recipes with eggs: {egg_recipes}")
