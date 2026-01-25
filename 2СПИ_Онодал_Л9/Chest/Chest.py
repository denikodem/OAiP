from abc import ABC, abstractmethod
from random import choice


class ChestAction(ABC):
    def __init__(self, config: "ChestConfig"):
        self.config = config

    @abstractmethod
    def execute(self):
        pass


class ChestConfig:
    MATERIALS = ("Дерево", "Медь", "Железо", "Золото", "Алмазы")

    def __init__(self, name):
        self.name = name
        self.is_open = True
        self.material_chest = choice(self.MATERIALS)
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
        return "Сундук был открыт" if self.config.is_open else "Сундук был закрыт"

    def __str__(self):
        return "Сундук открыт" if self.config.is_open else "Сундук закрыт"


class SetMaterial(ChestAction):
    def execute(self):
        try:
            choice = int(input("""\nВведите материал сундука
1. Дерево
2. Медь
3. Железо
4. Золото
5. Алмазы"""))
            self.config.material_chest = self.config.MATERIALS[choice - 1]
        except (ValueError, IndexError):
            return "Неверный код"
        return f'Материал сундука изменен на {self.config.material_chest}'

    def __str__(self):
        return f"Материал сундука: {self.config.material_chest}"


class SwitchDoubleChest(ChestAction):
    def execute(self):
        self.config.double_chest = not self.config.double_chest
        return "Сундук теперь двойной" if self.config.double_chest else "Сундук теперь одинарный"

    def __str__(self):
        return "Сундук двойной" if self.config.double_chest else "Сундук одинарный"


class AddInChest(ChestAction):
    def execute(self):
        if self.config.is_open:
            items = input('Напишите через пробел названия предметов>>>>').split()
            if not items:
                return "Предметы не были введены"
            self.config.items_inside.extend(items)
            return f"Предметы: {'; '.join(items)} добавлены в сундук"
        else:
            return f'Сундук был закрыт и предметы не были добавлены.'

    def __str__(self):
        return f"В сундуке: {', '.join(self.config.items_inside) if self.config.items_inside else 'пусто'}"
