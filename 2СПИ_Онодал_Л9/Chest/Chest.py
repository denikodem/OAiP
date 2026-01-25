from abc import ABC, abstractmethod
from random import choice


class ChestAction(ABC):
    def __init__(self, config: "ChestConfig"):
        self.config = config

    @abstractmethod
    def execute(self):
        pass


class ChestConfig:
    def __init__(self, name):
        self.material = ("Дерево", "Медь", "Железо", "Золото", "Алмазы")

        self.name = name
        self.is_open = True
        self.material_chest = choice(self.material)
        self.double_chest = False

        self.items_inside = []

    def __str__(self):
        return f"""
        Состояние сундука:
Название сундука: {self.name}
Состояние сундука: {"Открыт" if self.is_open else "Закрыт"}
Материал сундука: {self.material_chest}
Размер сундука: {"Двойной" if self.double_chest else "Одинарный"}
"""


class SwitchChest(ChestAction):
    def execute(self):
        self.config.is_open = not self.config.is_open

    def __str__(self):
        return "Сундук открыт" if self.config.is_open else "Сундук закрыт"


class SetMaterial(ChestAction):
    def execute(self):
        self.config.material_chest = self.config.material[int(input("""\nВведите материал сундука
1. Дерево
2. Медь
3. Железо
4. Золото
5. Алмазы""")) - 1]

    def __str__(self):
        return f"Материал сундука: {self.config.material_chest}"

class SetScale(ChestAction):
    def execute(self):
        self.config.double_chest = not self.config.double_chest
        return "Сундук теперь двойной" if self.config.double_chest else "Сундук теперь одинарный"

