import json
import os
import random

names = ['Иван', 'Константин', 'Алексей', 'Степан', 'Григорий']
surnames = ['Герасимов', 'Макаров', 'Никитин', 'Кузнецов', 'Борисов']
pnames = ['Олегович', 'Константинович', 'Васильевич', 'Николаевич', 'Иванович']
cities = ['Уфа', 'Благовещенск', 'Санкт-Петербург', 'Красноярск', 'Ханты-Мансийск']
places = ['Московский государственный университет', 'Лицей_7', 'Колледж программирования', 'Гимназия_42', 'Школа_902']

old = random.randint(1959, 2010)
num = random.randint(74950000000, 74959999999)

name = random.choice(names)
sname = random.choice(surnames)
pname = random.choice(pnames)
city = random.choice(cities)
edu = random.choice(places)

data = {
    'Фамилия': sname,
    'Имя': name,
    'Отчество': pname,
    'Телефон': num,
    'Год рождения': old,
    'Город рождения': city,
    'Место учебы': edu
}

with open("data.json", 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

os.startfile('data.json')
