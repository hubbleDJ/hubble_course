# Лекция 2025-01-22
# PEP8

# Int - Целое число
myIntVar = 1
myIntVar: int = 7
print(myIntVar * 90)
print(myIntVar + 90)
print(myIntVar - 90)
print(myIntVar / 90)
print(myIntVar ** 2)
print(myIntVar // 2) # Целая часть
print(myIntVar % 2) # Остаток от деления
print(myIntVar == 7)
print(myIntVar >= 7)
print(myIntVar <= 7)
print(myIntVar != 7)
print(not myIntVar == 7)


myIntVar = myIntVar + 1
myIntVar += 1
myIntVar -= 1
myIntVar /= 2
print(myIntVar)

# Float - Дробное число
myFloatVar = 1.7
myFloatVar: float = 1.7

# Bool - логический тип данных (True/False)
myBoolVar: bool = True

# List - список
myListVar: list[int] = [1, 2, 3, 4, 890, 0]
myListVar: list[int|float|list[int]] = [1, 2, 78.8, 3, 4, 890, 0, [1, 3]]
myListVar.append(990)

print(myListVar[1])
print(myListVar[1:5]) # Элементы 1, 2, 3, 4
print(myListVar[:3]) # Элементы 0, 1, 2
print(len(myListVar))

print(45 in [1, 3, 4, 67])

# String - Строка
myStringVar: str = "Hello,' world!"
myStringVar: str = 'Hello, world!'
myStringVar: str = '''Hello, world!'''
myStringVar: str = """Hello, world!"""

print(myStringVar[:5])
print('Hello,' + ' world!') # Конкатинация строк

x: int|float = 1
y: int|float = 100

print(int('765'))

print(str(x) + ' + ' + str(y) + ' = ' + str(x+y))
print('{} + {} = {}'.format(x, y, x+y))
print(f'{x} + {y} = {x+y}')

# Tuple - кортеж
myTupleVar: tuple = (1, 7)
myTupleVar: tuple = 1, 4, 5
print(myTupleVar[0])

# Set - множество
mySetVar: set = {1, 3, 4, 6}
mySetVar.add(7)
print(mySetVar)

# Frozenset - неизменяемый set
myFrozensetVar: frozenset = frozenset({1, 3, 4})

# Dict - Словарь
myDictVar: dict = {
    'name': 'Maks',
    'age': 27,
    'gender': 'M',
    'hobby': ['IT', 'Cars']
}

myDictVar['surname'] = 'Strometskiy'

print(myDictVar)
print(myDictVar['name'])
print(f'''Его зовут {myDictVar['name']}''')
print(myDictVar.get('id'))

print(type(myDictVar))
print(type(''))
print(dir(myDictVar))
print(myDictVar.values())
print(myDictVar.keys())
print('name' not in myDictVar)
print(myDictVar.items())

# print(help())

# input
my_value: str = input('Введите значение: ')
print(f'Вы ввели {my_value}')

print(print)

t = [(1, 3), 78]
