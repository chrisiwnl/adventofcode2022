from backpack import BackPack


class Elf:
    def __init__(self, name: str):
        self._name = name
        self.backpack = BackPack()

    @property
    def name(self):
        return self._name

    @property
    def backpack_content(self):
        return self.backpack.content

    def add_to_backpack(self, item):
        self.backpack.add_to_backpack(item)

    def calculate_calories_in_bag(self):
        calories = 0
        for food in self.backpack.content:
            calories += food.calories

        return calories

