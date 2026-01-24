from abc import ABC, abstractmethod

class ButtonAction(ABC):
    def __init__(self, config: "ButtonConfig"):
        self.config = config
    @abstractmethod
    def execute(self):
        pass

class ButtonConfig:
    def __init__(self):
        # атрибуты кнопки
        self.toggle = False
        self.scale = (1.0, 1.0)
        self.text = ""
        self.color = (0, 0, 0)

class TogglerButton(ButtonAction):
    def execute(self) -> bool:
        self.config.toggle = not self.config.toggle
        return self.config.toggle

class ScaleButton(ButtonAction):
    def execute(self) -> tuple[int, int]:
        x, y = map(int, input("Укажите размер кнопки X и Y через пробел\n>>>>> ").split(' '))
        self.config.scale = (x, y)
        return self.config.scale

class TextButton(ButtonAction):
    def execute(self) -> str:
        self.config.text = str(input())
        return self.config.text

class ColorButton(ButtonAction):
    def execute(self) -> tuple[int, int, int]:
        r, g, b = map(int, input("Укажите три цвета RGB через пробел\n>>>>>").split(" "))
        self.config.color = (r, g, b)
        return self.config.color
