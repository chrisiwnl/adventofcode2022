class Option:
    def __init__(self, name: str):
        self.name = name


class Rock(Option):
    def __init__(self):
        self.code = "X"
        self.enemy_code = "A"
        self.value = 1


class Paper(Option):
    def __init__(self):
        self.code = "Y"
        self.enemy_code = "B"
        self.value = 2


class Scissor(Option):
    def __init__(self):
        self.code = "Z"
        self.enemy_code = "C"
        self.value = 3
