"""Homework 2025-01-22 part 2"""

dataset: dict = {
    'name': '',
    'surname': '',
    'age': '',
    'sex': '',
    'hobby': '',
    'city': ''
}

dataset['name'] = input('Напишите ваше имя: ')
dataset['surname'] = input('Напишите вашу фамилию: ')
dataset['age'] = input('Сколько вам лет: ')
dataset['sex'] = input('Укажите ваш пол: ')
dataset['hobby'] = input('Напишите, чем вы увлекаетесь: ')
dataset['city'] = input('Напишите, где вы живете: ')

print(
    f'Имя {dataset.get("name", "Пользователь не указал имя")}, '
    f'а фамилия {dataset.get("surname", "Пользователь не указал фамилию")}'
)
print(
    f'Вот столько лет от роду: {dataset.get("age", "Пользователь не указал возраст")}')
print(f'Гендер: {dataset.get("sex", "Пользователь не указал пол")}')
print(f'Увлечения: {dataset.get("hobby", "Пользователь не указал хобби")}')
print(f'Живет - {dataset.get("city", "Пользователь не указал город")}')
