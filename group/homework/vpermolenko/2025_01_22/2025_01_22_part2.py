#homework2

myPerson: dict = {}

myPerson['name'] = input("Напиши как тебя зовут: ")
myPerson['gender'] = input("Твой пол: ")
myPerson['age'] = input("Возраст: ")
myPerson['meal'] = input("Твоё любимое блюдо: ")
myPerson['hobby'] = input("Какими хобби занимаешься?: ")

print(f'''Привет, {myPerson['gender']} {myPerson['name']}!
В свои {myPerson['age']} ты любишь кушать {myPerson['meal']} и занимаешься {myPerson['hobby']} - ты крут!''')