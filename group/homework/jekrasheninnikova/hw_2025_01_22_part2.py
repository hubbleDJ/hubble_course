"""Homework 2025-01-22 part 2"""

userInfo: dict = {}
userInfo['name'] = input('Как тебя зовут?\n')
userInfo['gender'] = input('Какой у тебя пол? Женский/Мужской\n')
userInfo['age'] = input('Сколько тебе лет?\n')
userInfo['hobby'] = input('Какие у тебя хобби? Введи три наиболее значимых для тебя\n'), input(), input()
userInfo['music'] = input(
    'Какая у тебя любимая музыка? '
    'Введи два наиболее интересных для тебя жанра/прилагательных\n'
), input()

print(
    f'''Привет, {userInfo['name']},'''
    f''' возраст которой {userInfo['age']} лет '''
    f'''и пол {userInfo['gender']},' \n'''
    f'''любящая {userInfo['hobby'][0]}, {userInfo['hobby'][1]} и {userInfo['hobby'][2]},' \n'''
    f'''слушающая {userInfo['music'][0]} и {userInfo['music'][1]}' '''
)
