from food import Food


class BackPack:
    def __init__(self):
        self.content = []

    @property
    def get_content(self):
        return self.content

    def add_to_backpack(self, item: Food):
        self.content.append(item)
