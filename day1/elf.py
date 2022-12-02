from backpack import BackPack


class Elf:
    def __init__(self, name: str):
        self.name = name
        self.backpack = BackPack()

    @property
    def get_name(self):
        return self.name

    @property
    def get_backpack_content(self):
        return self.backpack.get_content

    def add_to_backpack(self, item):
        self.backpack.add_to_backpack(item)

    def calculate_calories_in_bag(self):
        calories = 0
        for food in self.backpack.get_content:
            calories += food.get_calories

        return calories

