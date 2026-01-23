class WebButton:
    def __init__(self):

        # атрибуты кнопки
        self.toggler = False
        self.color = None
        self.scale = [1.0, 1.0]
        self.text = None

    def click_button(self):
        if not self.toggler:
            self.toggler = True
            print("Кнопка включена")
        else:
            self.toggler = False
            print("Кнопка выключена")

    