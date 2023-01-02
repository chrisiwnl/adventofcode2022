from food import Food


class BackPack:
    def __init__(self):
        self._content = []

    @property
    def content(self):
        return self._content

    def add_to_backpack(self, item: Food):
        self.content.append(item)
