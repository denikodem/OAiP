class StatsPet:
    def __init__(self):
        """
        Статистика питомца
        здоровье если уменьшится до 0 игра окончена
        счастье, голод, обезвоживание и сонливость будут опускать
        значение здоровья по одной при достижении высоких значений
        чем меньше сложность тем сложнее играть
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
            Так же есть параметр ходы, это 
            """
        )


class InteractionsPet(StatsPet):

    def start_game(self):
        self.name = str(input("Имя питомца?\n>>> "))
        self.difficulty = int(input("Сложность 1-3\n>>> "))
        print(f"Вы назвали своего питомца именем: {self.name}")
        print(f"Вы выбрали сложность игры: {self.difficulty}")

    def show_stats(self):
        print({
        "Имя": self.name,
        "Счастье": self.happiness,
        "Здоровье": self.health,
        "Голод": self.hunger,
        "Обезвоживание": self.dehydration,
        "Сонливость": self.sleepiness,
        "Счет игры": self.score
        })

    def feed_pet(self):
        self.hunger -= 3 * self.difficulty
        self.dehydration += self.difficulty
        self.sleepiness += self.difficulty
        self.end_turn()
        print(f"{self.name} поел")

    def drink_pet(self):
        self.dehydration -= 3 * self.difficulty
        self.hunger += self.difficulty
        self.sleepiness += self.difficulty
        self.end_turn()
        print(f"{self.name} попил")

    def sleep_pet(self):
        self.sleepiness -= 3 * self.difficulty
        self.hunger += self.difficulty
        self.dehydration += self.difficulty
        self.happiness -= self.difficulty
        self.end_turn()
        print(f"{self.name} поспал")

    def play_pet(self):
        self.happiness += 2 * self.difficulty
        self.hunger += self.difficulty
        self.dehydration += self.difficulty
        self.sleepiness += self.difficulty
        self.end_turn()
        print(f"{self.name} поиграл")

    def end_turn(self):
        self.score += 1
        self.health_check()
        self.check_stats()

    def health_check(self):
        if self.hunger == 10:
            self.health -= 1
        if self.dehydration == 10:
            self.health -= 1
        if self.sleepiness == 10:
            self.health -= 1
        if self.happiness == 0:
            self.health -= 1
        if self.health <= 0:
            self.game_over()

    def check_stats(self):
        self.hunger = max(0, min(10, self.hunger))
        self.dehydration = max(0, min(10, self.dehydration))
        self.sleepiness = max(0, min(10, self.sleepiness))
        self.happiness = max(0, min(10, self.happiness))

    def game_over(self):
        print(
            f"""
            ИГРА ОКОНЧЕНА, ВЫ ПРОИГРАЛИ
            Ваш счет: {self.score}
            """
        )
        #self.running = 0
        #input("Нажмите Enter для выхода...")