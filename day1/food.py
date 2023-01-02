class Food:
    def __init__(self, calories: int):
        self._calories = calories
        self._name = ""

    @property
    def calories(self):
        return self._calories

    @property
    def name(self):
        return self._name

    @staticmethod
    def form(name):
        if name in ["Bread", "Pizza", "Chocolate"]:
            return "Solid"
        else:
            return "Liquid"
