import json

# чтение файла #
with open('people.json', 'r', encoding='utf-8') as f:
    people = json.load(f)
# для списка людей живущих в москве #
names = []
ages = []

# проверка людей которые живут в москве #
for person in people.values():
    if person["city"] == "Moscow":
        names.append(person["name"])
        ages.append(person["age"])

#Вывод на экран списка проживающих в москве #
print("Имена:", ', '.join(names))
if ages:
    # Вывод среднего возраста с округлением #
    print(f"Средний возраст: {round(sum(ages) / len(ages))}")
else:
    # на случай если москвичей нет #
    print("Нет людей из Москвы")
