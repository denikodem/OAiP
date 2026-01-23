from Tamagochi import (
    TamagochiGame,
    FeedAction,
    DrinkAction,
    SleepAction,
    PlayAction
)


def main():
    game = TamagochiGame()

    actions = {
        "1": FeedAction(),
        "2": DrinkAction(),
        "3": SleepAction(),
        "4": PlayAction()
    }

    game.start_game()

    while game.health > 0 and game.score < game.WINSCORE:
        game.show_stats()

        print("""        1 - Покормить
        2 - Напоить
        3 - Уложить спать
        4 - Поиграть
        5 - Правило""")

        choice = input(">>> ")

        if choice in actions:
            actions[choice].execute(game)
        elif choice == 5:
            game.rules_game()
        else:
            print("Неверный выбор, попробуйте ещё раз")
            continue

    game.end_game()
if __name__ == "__main__":
    main()

input("Нажмите Enter для выхода...")
