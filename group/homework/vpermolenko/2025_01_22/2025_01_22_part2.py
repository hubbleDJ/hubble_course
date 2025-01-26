"""Module homework2"""

person: dict = {}

person['name'] = input("Напиши как тебя зовут: ")
person['gender'] = input("Твой пол: ")
person['age'] = input("Возраст: ")
person['meal'] = input("Твоё любимое блюдо: ")
person['hobby'] = input("Какими хобби занимаешься?: ")

print(f'''Привет, {person['gender']} {person['name']}!
В свои {person['age']} ты любишь кушать {person['meal']}
и занимаешься {person['hobby']} - ты крут!''')
