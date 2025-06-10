import json
import os

with open("data.json", 'r', encoding='utf-8') as f:
    data = json.load(f)

a = int(input('''
    Что желаете изменить?
    
    1. Фамилию
    2. Имя
    3. Отчество
    4. Телефон
    5. Год рождения
    6. Город рождения
    7. Место учебы
    
>>>>> '''))


redact = input('''
Что на какие данные желаете заменить?
>>>>> ''')

data_red = ""

if a == 1:
    data_red = "Фамилия"

elif a == 2:
    data_red = "Имя"

elif a == 3:
    data_red = "Отчество"

elif a == 4:
    data_red = "Телефон"

elif a == 5:
    data_red = "Год рождения"

elif a == 6:
    data_red = "Город рождения"

elif a == 7:
    data_red = "Место учебы"

data[data_red] = redact

with open("data.json", 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

os.startfile('data.json')
