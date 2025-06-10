# перенос файла в переменную #
file = open('words.txt', 'r', encoding='utf-8')
# создание списка из строк удаляя перенос строки #
lines = [line.rstrip('\n') for line in file]
# поиск максимальной длины строки #
max_len = max(len(line) for line in lines)
# вывод строк равных максимальной длине строки #
for line in lines:
    if len(line) == max_len:
        print(line)
