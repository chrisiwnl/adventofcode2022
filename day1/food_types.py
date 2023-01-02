from food import Food


class Bread(Food):
    def __init__(self, calories: int):
        super().__init__(calories)
        self._name = "Bread"


class Milk(Food):
    def __init__(self, calories: int):
        super().__init__(calories)
        self._name = "Milk"

    @staticmethod
    def form():
        return "Liquid"


class Chocolate(Food):
    def __init__(self, calories: int):
        super().__init__(calories)
        self._name = "Chocolate"


class Pizza(Food):
    def __init__(self, calories: int, ingreds: list):
        super().__init__(calories)
        self._name = "pizza"
        self._ingredients = ingreds

    def __eq__(self, other):
        if self._name == other:
            return True

    @classmethod
    def hawaii(cls):
        return cls(150, ["cheese", "ananas", "pepperoni"])

    @property
    def ingredients(self):
        return self._ingredients
