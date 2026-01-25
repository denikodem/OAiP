from Chest import (
    ChestConfig,
    SwitchChest,
    SetMaterial,
    SwitchDoubleChest,

)

class ManagerClass:

    name_chest = str(input("Дайте название своему сундуку\n>>> "))

    def __init__(self):
        self.obj = ChestConfig(self.name_chest)
        self.action = SetMaterial(self.obj)

        self._choices = """
    Выберете действие:
1. Открыть сундук
2. Поменять материал сундука
3. Поменять размер сундука
4. Посмотреть что внутри
5. Добавить предмет
6. Удалить предмет
7. Выход
"""
    map_action = {
        "1": SwitchChest,
        "2": SetMaterial,
        "3": SwitchDoubleChest,
        "4":
    }

    def run(self):
        print("\n\nДОБРО ПОЖАЛОВАТЬ В CHEST FROM GAME\n")
        while True:
            choice = input(self._choices)
            if choice in self.map_action:
                result = self.map_action[choice].execute(self.action)
                print(result)
            elif choice == "7":
                break
            else:
                continue

if __name__ == "__main__":
    ManagerClass.run()
    input("\n\nНажмите Enter чтобы выйти...")