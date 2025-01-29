userInfo: dict = {}
userInfo['name'] = input(f'Как тебя зовут?\n')
userInfo['gender'] = input(f'Какой у тебя пол? Женский/Мужской\n')
userInfo['age'] = input(f'Сколько тебе лет?\n')
userInfo['hobby'] = input(f'Какие у тебя хобби? Введи три наиболее значимых для тебя\n'), input(), input()
userInfo['music'] = input(f'Какая у тебя любимая музыка? Введи два наиболее интересных для тебя жанра/прилагательных\n'), input()
print(
    f'''Привет, {userInfo['name']},'''
    f''' возраст которой {userInfo['age']} лет '''
    f'''и пол {userInfo['gender']},' \n'''
    f'''любящая {userInfo['hobby'][0]}, {userInfo['hobby'][1]} и {userInfo['hobby'][2]},' \n'''
    f'''слушающая {userInfo['music'][0]} и {userInfo['music'][1]}' '''
)
