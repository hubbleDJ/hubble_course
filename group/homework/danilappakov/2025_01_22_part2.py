dataset: dict = {
    "name": "",
    "surname": "",
    "district": "",
    "age": "",
    "favorite_place": "",
    "transport": "",
    "famous_event": "",
    "reason_to_leave": ""
}

dataset["name"] = input("Как тебя зовут? ")
dataset["surname"] = input("Какая у тебя фамилия? ")
dataset["district"] = input("В каком районе Омска ты живешь? ")
dataset["age"] = int(input("Сколько лет ты прожил в Омске? "))
dataset["favorite_place"] = input("Какое место в Омске тебе нравится больше всего? ")
dataset["transport"] = input("Каким видом транспорта ты чаще всего передвигаешься по городу? ")
dataset["famous_event"] = input("Какое известное событие или факт об Омске ты знаешь? ")
dataset["reason_to_leave"] = input("Если бы ты уехал из Омска, то почему? ")


print(f"Имя: {dataset.get('name')} {dataset.get('surname')}")
print(f"Район проживания: {dataset.get('district')}")
print(f"Время, проведенное в Омске: {dataset.get('age')} лет")
print(f"Любимое место в городе: {dataset.get('favorite_place')}")
print(f"Предпочитаемый транспорт: {dataset.get('transport')}")
print(f"Знаменитый факт об Омске: {dataset.get('famous_event')}")
print(f"Причина, по которой ты мог бы уехать из Омска: {dataset.get('reason_to_leave')}")