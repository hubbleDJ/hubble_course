dataset: dict = {
    "name": " ",
    "surname": " ",
    "age": " ",
    "mother": " ",
    "father": " ",
    "country": " "
}

dataset["name"] = input('Имя?')
dataset["surname"] = input('Фамилия?')
dataset["age"] = int(input('Сколько тебе лет?'))
dataset["mother"] = input('Как зовут маму?')
dataset["father"] = input('Как зовут отца?')
dataset["country"] = input('В какой ты стране?')

print(f'Имя {dataset.get("name")}, а фамилия {dataset.get("surname")}')
print(f'Вот столько лет от роду {dataset.get("age")}')
print(f'Твою маму зовут: {dataset.get("mother")}')
print(f'Твоего отца зовут: {dataset.get("father")}')
print(f'Ты живёшь в: {dataset.get("country")}')