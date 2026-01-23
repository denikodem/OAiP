class StatsTamagotchi:
    def __init__(self):
        """
        Статистика питомца
        здоровье если уменьшится до 0 игра окончена
        счастье, голод, обезвоживание и сонливость будут опускать
        значение здоровья по одной при достижении высоких значений
        чем меньше сложность тем сложнее играть
        """
        self.name = None

        self.health = 10
        self.fanny = 10
        self.hunger = 0
        self.dehydration = 0
        self.sleepiness = 0

        self.difficulty = 1

class InteractionsPet(StatsTamagotchi):

    def give_name(self):
        self.name = str(input(">>> "))
        print(f"Вы назвали своего питомца именем {self.name}")

    def snow_stats(self):
        return {
        "Имя": self.name,
        "Счастье": self.fanny,
        "Здоровье": self.health,
        "Голод": self.hunger,
        "Обезвоживание": self.dehydration,
        "Сонливость": self.sleepiness,
        }

    def feed_pet(self):

        self.hunger -= (2 * self.difficulty)
        print(f"{self.name} поел")

    def drink_pet(self):
        self.dehydration -= (2 * self.difficulty)
        print(f"{self.name} попил")

    def sleep_pet(self):
        self.sleepiness -= (2 * self.difficulty)
        print(f"{self.name} поспал")

class OutputText:
    @staticmethod
    def hello_user():
        print(
            """
            ДОБРО ПОЖАЛОВАТЬ В ИГРУ ТАМАГОЧИ!
            как желаете назвать своего питомца?
            """
        )
    @staticmethod
    def rules_game():
        print(
            """
            ПРАВИЛА ИГРЫ:
            В начале вы выбираете имя питомца
            Дальше ваш питомец будет требовать ухода
            У питомца будет несколько параметров:
                * Здоровье - если оно опустится до 0 вы проиграете
                * Счастье, Голод, Обезвоживание и Сонливость будут наносить урон если дойдут до 10
                * Сложность влияет на количество получаемого/опускаемого значения (2 * Сложность)
            Помните каждое действие с питомцем может как дать нужное значение так и забрать другое
            """
        )
    @staticmethod
    def game_over():
        print(
            """
            ИГРА ОКОНЧЕНА, ВЫ ПРОИГРАЛИ
            """
        )
