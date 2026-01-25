from Chest import (
    ChestConfig,
    SwitchChest,
    SetMaterial,
)
choices = """
    Выберете действие:
1. Открыть сундук
2. Поменять материал сундука
3. Поменять размер сундука
4. Посмотреть что внутри
5. Добавить предмет
6. Удалить предмет
"""
map_action = {
    "1": SwitchChest,
    "2": SetMaterial,
    "3": '',
}

def main():
    print("\n\nДОБРО ПОЖАЛОВАТЬ В CHEST FROM GAME\n")
    name_chest = str(input("Дайте название своему сундуку\n>>> "))

    obj = ChestConfig(name_chest)
    action = SetMaterial(obj)
    running = True

    while running:
        choice = int(input(choices))

if __name__ == "__main__":
    main()
    input("\n\nНажмите Enter чтобы выйти...")