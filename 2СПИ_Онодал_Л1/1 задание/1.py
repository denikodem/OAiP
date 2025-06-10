from random import randrange

# чтение строк файла в переменую #
text_lines = open('lines.txt', encoding='utf-8').readlines()

# если файл пустой то выведет "Пустой файл" #
if not text_lines:
    print('* Пустой файл *')
# Иначе индексация строк и выбор рандомной строки #
else:
    line = randrange(len(text_lines))
    # если рандомная строка пуста то выведет "Пустая строка" #
    if text_lines[line] == '\n':
        print('* Пустая строка *')
    # Иначе вывод рандомной строки #
    else:
        print(text_lines[line])
