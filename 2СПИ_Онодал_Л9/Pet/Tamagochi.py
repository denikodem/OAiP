from abc import ABC, abstractmethod


class ActionPattern(ABC):
    @abstractmethod
    def _do_interaction(self, pet):
        raise NotImplementedError("Метод _do_interaction обязателен в классе-действии с питомцем!")

    def execute(self, pet):
        self._do_interaction(pet)
        pet.end_turn()


class TamagochiGame:
    def __init__(self):
        """
        Статистика питомца
        здоровье если уменьшится до 0 игра окончена
        счастье, голод, обезвоживание и сонливость будут опускать
        значение здоровья по одной при достижении высоких значений
        чем меньше сложность тем дольше играть
        счет - количество действий или же счет игры
        """
        self.name = None
        self.health = 10
        self.happiness = 10
        self.hunger = 0
        self.dehydration = 0
        self.sleepiness = 0
        self.difficulty = 1

        self.score = 0
        self.WINSCORE = 50

    def start_game(self):
        self.hello_user()
        self.name = str(input("Имя питомца?\n>>> "))
        self.difficulty = int(input("Сложность 1-3\n>>> "))
        self.difficulty = max(1, min(3, self.difficulty))
        print(f"Вы назвали своего питомца именем: {self.name}")
        print(f"Вы выбрали сложность игры: {self.difficulty}")

    def show_stats(self):
        print(f"""
        Имя: {self.name}
        Счастье: {self.happiness}
        Здоровье: {self.health}
        Голод: {self.hunger}
        Обезвоживание: {self.dehydration}
        Сонливость: {self.sleepiness}
        Счет игры: {self.score}
        """)

    def end_turn(self):
        self.score += 1
        self.check_stats()
        self.health_check()

    def health_check(self):
        if self.hunger >= 10:
            self.health -= 1
        if self.dehydration >= 10:
            self.health -= 1
        if self.sleepiness >= 10:
            self.health -= 1
        if self.happiness <= 0:
            self.health -= 1

    def check_stats(self):
        self.hunger = max(0, min(10, self.hunger))
        self.dehydration = max(0, min(10, self.dehydration))
        self.sleepiness = max(0, min(10, self.sleepiness))
        self.happiness = max(0, min(10, self.happiness))

    def end_game(self):
        if self.health <= 0:
            print(
                f"""
            ИГРА ОКОНЧЕНА, ВЫ ПРОИГРАЛИ
            Ваш счет: {self.score}
            """)
        elif self.score >= self.WINSCORE:
            print(f"""
            ПОЗДРАВЛЯЕМ! ВЫ ВЫИГРАЛИ!
            Ваш счет достиг 50 и вы прошли игру!\n\n""")

    @staticmethod
    def hello_user():
        print(
            """
            ДОБРО ПОЖАЛОВАТЬ В ИГРУ ТАМАГОЧИ!
            выберете имя питомцу и уровень сложности
            чем меньше сложность тем дольше играть
            """
        )

    @staticmethod
    def rules_game():
        print("""
    *********************************************************************************************
    *                                   ПРАВИЛА ИГРЫ:                                           *
    *    В начале вы выбираете имя питомца                                                      *
    *    и сложность игры, которая влияет на продолжительность игры                             *
    *    Дальше ваш питомец будет требовать ухода                                               *
    *    У питомца будет несколько параметров:                                                  *
    *       - Здоровье - если оно опустится до 0 вы проиграете                                  *
    *       - Счастье, Голод, Обезвоживание и Сонливость будут наносить урон если дойдут до 10  *
    *       - Сложность влияет на количество получаемого/опускаемого значения (3 * Сложность)   *
    *    Помните каждое действие с питомцем может как дать нужное значение так и забрать другое *
    *    Вы победите если достигните 50 очков счета                                             *
    *********************************************************************************************"""
              )


class FeedAction(ActionPattern):
    def _do_interaction(self, pet: TamagochiGame):
        pet.hunger -= 3 * pet.difficulty
        pet.dehydration += pet.difficulty
        pet.sleepiness += pet.difficulty
        pet.happiness -= pet.difficulty
        print(f"{pet.name} поел")


class DrinkAction(ActionPattern):
    def _do_interaction(self, pet: TamagochiGame):
        pet.dehydration -= 3 * pet.difficulty
        pet.hunger += pet.difficulty
        pet.sleepiness += pet.difficulty
        pet.happiness -= pet.difficulty
        print(f"{pet.name} попил")


class SleepAction(ActionPattern):
    def _do_interaction(self, pet: TamagochiGame):
        pet.sleepiness -= 3 * pet.difficulty
        pet.hunger += pet.difficulty
        pet.dehydration += pet.difficulty
        pet.happiness -= pet.difficulty
        print(f"{pet.name} поспал")


class PlayAction(ActionPattern):
    def _do_interaction(self, pet: TamagochiGame):
        pet.happiness += 3 * pet.difficulty
        pet.hunger += pet.difficulty
        pet.dehydration += pet.difficulty
        pet.sleepiness += pet.difficulty
        print(f"{pet.name} поиграл")
