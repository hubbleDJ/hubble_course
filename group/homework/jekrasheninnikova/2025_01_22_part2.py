myData: dict = {}
myData['name'] = input(f'Как тебя зовут?\n')
myData['gender'] = input(f'Какой у тебя пол? Женский/Мужской\n')
myData['age'] = input(f'Сколько тебе лет?\n')
myData['hobby'] = input(f'Какие у тебя хобби? Введи три наиболее значимых для тебя\n'), input(), input()
myData['music'] = input(f'Какая у тебя любимая музыка? Введи два наиболее интересных для тебя жанра/прилагательных\n'), input()
print(f'''Привет, {myData['name']}, возраст которой {myData['age']} лет и пол {myData['gender']}, любящей {myData['hobby'][0]}, {myData['hobby'][1]} и {myData['hobby'][2]}, слушающая {myData['music'][0]} и {myData['music'][1]}''')
