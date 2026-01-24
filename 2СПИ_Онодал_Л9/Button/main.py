from fastapi.params import Cookie

from Button import (
    ButtonConfig,
    TogglerButton,
    ScaleButton,
    TextButton,
    ColorButton,
)


class ButtonManager:
    def __init__(self):
        self.config = ButtonConfig()
        self.buttons = {
            "1": TogglerButton(self.config),
            "2": ScaleButton(self.config),
            "3": TextButton(self.config),
            "4": ColorButton(self.config)
        }

    def run(self):
        running = True
        while running:
            choice = input("""
            Выберите действие с кнопкой:
            
            1. Включить/Выключить
            2. Изменить размеры кнопки
            3. Поменять текст кнопки
            4. Поменять цвет кнопки
            5. Показать конфиг кнопки
            6. Выход
            
>>>>""")
            if choice == "6":
                running = not running
            elif choice == "5":
                print(ButtonConfig.give_config(self.config))
            elif choice in self.buttons:
                result = self.buttons[choice].execute()
                print("Получилось: ", result)
            else:
                print("Повторите попытку")
                continue


if __name__ == "__main__":
    ButtonManager().run()
    input('Нажмите Enter для выхода...')
