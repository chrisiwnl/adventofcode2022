class Food:
    def __init__(self, calories: int):
        self.calories = calories

    @property
    def get_calories(self):
        return self.calories
