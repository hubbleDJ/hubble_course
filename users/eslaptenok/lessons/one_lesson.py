import datetime

# Переменные
var_int: int = 1
var_float: float = 0.0

var_str: str = 'Maks'
var_str: str = "Maks"
var_str: str = '''Maks'''
var_str: str = """Maks"""

var_bool: bool = True
var_bool: bool = False

# Коллекции

var_list: list[int] = [1, 2, 3]
var_list: list[int] = [0]
var_list: list[int | str] = [0, 'lol']
var_list: list = [[1, 4], [2, 5]]

var_tuple: tuple[int] = (1, 2, 3)
var_tuple: tuple[int] = (1,)

var_set: set[int] = {1, 3, 3}
var_set: set = set()

var_dict: dict[str, str] = {
    'key': 'value',
}

var_none = None

print(6 / 4)
print(int(6 / 4))
print(6 // 4)
print(6 % 4)


print('Hello' + ' ' + 'world!')
print('Число var_int = {}'.format(var_int))
print(f'Число var_int + 1 = {var_int + 1}')

print('''
    lkl
    vlbkhjdj
    'vbdkjhg's
    "vbldkjhfhj"
    """fvfdv"""
''')

if 'var_int':
    print('olo')

print(bool(''))

numbers: list[int] = [112, 354, 64, 0]
numbers[1] = 878
numbers.append(3)
numbers.pop(0)
numbers.remove(878)
print(numbers[0])

print(dir(1))
# print(help(numbers.reverse))
print(numbers[0:2])
print(numbers[:])
print(numbers[:2])
print(numbers[:-1])

print('jfvhhdfkjvhdfkhbvjkfdhjkbvhdfsj'[:5])

numbers_tup: tuple[int] = (112, 354, 64, 0)
print(numbers_tup[0: 5])
# print(numbers_tup.append(0)) - НЕЛЬЗЯ

numbers_set: set[int] = set(numbers_tup)
print(numbers_set)
numbers_set.add(12348)
print(numbers_set)
print(set([1, 2, 3, 4]) & set([1, 4, 7]))
for number in numbers_set:
    print(number)

print()
people: dict = {
    'id': 0,
    'name': 'Maks',
    'age': 27,
    'hobby': ['car', 'karting', 'it'],
    'family': {
        'mama': 1,
        'papa': 2
    }
}

print(people['age'])
people['gender'] = 'M'
print(people['family']['papa'])


print(people.keys())
print(people.values())
print(people.items())
