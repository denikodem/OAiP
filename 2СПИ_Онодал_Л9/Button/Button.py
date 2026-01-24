class WebButton:
    def __init__(self):
        # атрибуты кнопки
        self.toggle = False
        self.scale = [1.0, 1.0]
        self.text = None
        self.color = None

    def toggle_button(self) -> bool:
        self.toggle = not self.toggle
        return self.toggle

    def scale_button(self) -> list:
        x, y = map(int, input("Укажите размер кнопки X и Y через пробел\n>>>>> ").split(' '))
        self.scale = [x, y]
        return self.scale

    def text_button(self) -> str:
        self.text = str(input())
        return self.text

    def color_button(self):
        r, g, b = map(int, input("Укажите три цвета RGB через пробел\n>>>>>").split(" "))
        self.color = [r, g, b]
        return self.color
