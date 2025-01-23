dataset: dict = {
    "name": " ",
    "surname": " ",
    "age": " ",
    "sex": " ",
    "hobby": " ",
    "city": " "
}

dataset["name"] = input('Имя?')
dataset["surname"] = input('Фамилия?')
dataset["age"] = int(input('Возраст?'))
dataset["sex"] = input('Пол?')
dataset["hobby"] = input('Чем увлекаешься?')
dataset["city"] = input('Где живешь?')

print(f'Имя {dataset.get("name")}, а фамилия {dataset.get("surname")}')
print(f'Вот столько лет от роду {dataset.get("age")}')
print(f'Гендер {dataset.get("sex")}')
print(f'Увлечения {dataset.get("hobby")}')
print(f'Живет {dataset.get("city")}')