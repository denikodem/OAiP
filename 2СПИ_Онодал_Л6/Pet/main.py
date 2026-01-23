from Tamagotchi import InteractionsPet

obj = InteractionsPet()

if __name__ == "__main__":

    obj.start_game()

    while obj.health > 0:
        if obj.score >= obj.WINSCORE:
            break
        obj.show_stats()
        print("""        1 - Покормить
        2 - Напоить
        3 - Уложить спать
        4 - Поиграть
        5 - Правило""")
        choice = input(">>> ")

        if choice == "1":
            obj.feed_pet()
        elif choice == "2":
            obj.drink_pet()
        elif choice == "3":
            obj.sleep_pet()
        elif choice == "4":
            obj.play_pet()
        elif choice == "5":
            obj.rules_game()
        else:
            print("Неверный выбор, попробуйте ещё раз")
            continue

    obj.end_game()

input("Нажмите Enter для выхода...")
