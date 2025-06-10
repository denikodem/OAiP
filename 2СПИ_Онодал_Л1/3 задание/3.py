# занесение строк прочитанного файла #
lines = open('lines.txt', 'r', encoding='utf-8').readlines()
# вывод четных строк с помощью цикла #
print('\nЧетные строки:\n')
for i in range(1, len(lines), 2):
    print(lines[i].strip())
# вывод нечетных строк с помощью цикла #
print('\nНе четные строки:\n')
for f in range(0, len(lines), 2):
    print(lines[f].strip())
