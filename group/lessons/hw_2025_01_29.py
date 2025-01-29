TOKEN: str = ''
name_file: str = __name__

# if __name__ == "__main__":
#     l = 123
#     print(__name__)
#     print("Hello, world!")
    
# print(l)

# my_num: int = int(input('ВВедите число от 0 до 100: '))

# if (my_num >= 0 and my_num <= 100) or my_num == 234545445:
#     print('Молодец')
# elif my_num < 0:
#     print('Число меньше 0. Введи другое')
# else:
#     print('Число больше 100. Введи другое')

# print(my_num >= 0 or my_num <= 100)

# inc: int = 0

# while inc <= 100:
#     print(inc)
#     inc += 1
    
# print(list(range(0, 101)))

# for inc in range(0, 101):
#     print(inc)

users: list[int] = [1, 5464354534, 56434, 56456344, 87968]

# print(users[0])

for i in range(0, len(users), 2):
    print(users[i])
    
for user in users:
    print(user)

user_info: dict = {
    'name': 'Maks',
    'age': 27,
    'gender': 'M',
    'hobby': ['IT', 'Cars']
}

# print(dir(user_info))

print('-------------------------')

for key in user_info.keys():
    print(key)
    
print('-------------------------')

for key in user_info:
    print(key)

print('-------------------------')
    
for value in user_info.values():
    print(value)
    
print('-------------------------')
    
for key, value in user_info.items():
    print(f'{key}: {value}')



users: list = [
    {
        'id': 0,
        'name': 'Maks',
        'age': 27,
        'gender': 'M',
        'hobby': ['IT', 'Cars']
    }, {
        'id': 1,
        'name': 'Den',
        'age': 18,
        'gender': 'M',
        'hobby': ['IT', 'Plov']
    }   
]


allAge: int = -1

for user in users:
    if 'age' in user and allAge > 0:
        allAge += user['age']
    else:
        allAge = user['age']

print(allAge)

hobbyCount: dict[str, int] = {}

for user in users:
    if 'hobby' in user:
        for hobby in user['hobby']:
            if hobby in hobbyCount:
                hobbyCount[hobby] += 1
            else:
                hobbyCount[hobby] = 1
                
print(hobbyCount)
print(hobbyCount.get('15314', 0))


inc: int = 100
while True:
    inc -= 1
    print(inc)
    
    if inc <= 0:
        break
    
answer: int = 0

for i in range(0, 100):
    answer += i
    
    if i % 2 == 0:
        continue
    
    answer += i

# exit()

print(answer)

chetNums: list[int] = []

for i in range(0, 1001):
    if i % 2 == 0:
        chetNums.append(i)


print(chetNums)

chetNums: list[int] = [i for i in range(1001) if i % 2 == 0]
print('---------------------------------')
print(chetNums)
print('---------------------------------')
print({ # Куда положить
    i # Что положить
    for i in range(1001) # откуда взять
    if i % 2 == 0 # При каких условиях
})
print({i for i in range(1001) if i % 2 == 0})
print('---------------------------------')
print({str(id): id for id in range(90000)})

