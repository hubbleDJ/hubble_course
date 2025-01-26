userinfo: dict = {}
userinfo['name'] = input(f'Как тебя зовут?\n')
userinfo['gender'] = input(f'Какой у тебя пол? Женский/Мужской\n')
userinfo['age'] = input(f'Сколько тебе лет?\n')
userinfo['hobby'] = input(f'Какие у тебя хобби? Введи три наиболее значимых для тебя\n'), input(), input()
userinfo['music'] = input(f'Какая у тебя любимая музыка? Введи два наиболее интересных для тебя жанра/прилагательных\n'), input()
print(f'''Привет, {userinfo['name']}, возраст которой {userinfo['age']} лет и пол {userinfo['gender']},' \n
любящая {userinfo['hobby'][0]}, {userinfo['hobby'][1]} и {userinfo['hobby'][2]},' \n
слушающая {userinfo['music'][0]} и {userinfo['music'][1]}'\n''')
