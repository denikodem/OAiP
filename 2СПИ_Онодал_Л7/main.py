# Лабораторная работа №7 #
# Вызов всех заданий на выбор #

from Glasn import count_vowels
from factorial import factorial
from fiba import fibonacci
from max_num import max_num
from prost_sloz import prost_sloz


def main():
    test_num = int(input('''    * * * * * * * * * * * * * * * * * *
    * Какое нужно задание?            *
    *  выберите нужный номер задания  *
    * 1. Нахождение факториала числа  *
    * 2. N-ное число Фибоначчи        *
    * 3. Поиск гласных букв в тексте  *
    * 4. Просто/сложное число         *
    * 5. Максимальное число в списке  *
    * Для выхода введите любой символ *
    * * * * * * * * * * * * * * * * * *

>>>>> '''))

    # Делить строку str(number) на нужную длину int(width) #
    # если не указывать число в width то придется сделать это в вызове функции #
    # в таком случае строка будет нужной длины
    def print_long_number(number, width=50):
        s = str(number)
        for i in range(0, len(s), width):
            # если убрать '+ width' или заменить на число #
            # то длина строки будет заданным числом #
            # если при замене '+ width' не менять в остальном коде #
            # то в конце конечного ответа будет разная длина строк, например пирамидкой #
            print(s[i:i + width])

    if test_num == 1:
        # int - для вывода неформатированного числа #
        # float - для вывода форматированного числа #
        # ввод от 0 до 997 из-за ограничения вывода символов #
        a = int(input("\nВведите число в диапазоне от 0 до 996\n\n>>> "))
        otvet = factorial(a)
        # вызов функции деления строки нужного ответа #
        print_long_number(otvet)

    elif test_num == 2:
        a = int(input("\nВведите число:\n\n>>> "))
        print(fibonacci(a))

    elif test_num == 3:
        a = input('\nВведите нужный текст\n\n>>> ')
        b = input('''
    Из какого языка гласные?
    1. Русский язык (а, е, ё, и, о, у, ы, э, ю, я)
    2. Английский язык (a, e, i, o, u)
    3. Немецкий язык (a, e, i, o, u, ä, ö, ü)
    4. Все эти три языка
    Введите любой символ для выхода\n
>>> ''')
        if b == "1":
            vowels = 'аеёиоуыэюя'
        elif b == "2":
            vowels = 'aeiou'
        elif b == "3":
            vowels = 'aeiouäöü'
        elif b == "4":
            vowels = 'аеёиоуыэюяaeiouaeiouäöü'
        else:
            quit()
        print(f'в тексте: {count_vowels(a, vowels)} гласных')

    elif test_num == 4:
        a = int(input('\nВведите число\n\n>>> '))
        otvet = prost_sloz(a)
        if otvet:
            print('\nЧисло является простым')
        else:
            print('\nЧисло является сложным')

    elif test_num == 5:
        a = list(map(int, input("Введите числа через пробел: ").split()))
        print(f'Максимальное число в списке: {max_num(a)[0]}\n')

    else:
        quit()


if __name__ == '__main__':
    main()

exit_input = input('\n\nнажмите Enter для завершение работы программы...')
