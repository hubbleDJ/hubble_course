# Коллекции

# Строка это тоже коллекция
text = 'Макс'
# Обращение по индексу
print(text[0])

# Список это связанный список (i элемент помнит, где лежит i+1)
my_list = [0, 3, 678, 'lol']

# Обращение по индексу
my_list[1]

# Добавление элемента
my_list.append(89)

# Удаление элемента
my_list.pop(3)
print(my_list)


collect = [1, 3, 678]

# Более быстрые коллекции
tuple() # Кортеж(По факту массив) - быстрее, чем список. Нельзя изменять
set() # Хеш сет - самая быстрая коллекция. Можно изменять. Нельзя обращаться по индексу

# Сет можно перебирать циклом
my_set = set()
for value in my_set:
    pass


# Положи в value знаечние из коллекции
for value in collect:
    print(value)

# range тоже возвращяет коллекцию
for i in range(0, len(collect)):
   collect[i]
   
# У словаря вместо индексов ключи
my_dict = {
    'lol': 1,
    'kek': 2,
    'cheburek': 67
}

# обращение идентично
print(my_dict['lol'])
print(my_list[0])


my_string = 'Строка'.lower()

# Переменные в классе - свойства класса/объекта класса
# Функции в классе - методы класса/объекта класса

class People:
    """
    Пример создания класса people
    """
    
    def __init__(self, name: str, age: int, gender: str) -> None:
        self.name = name
        self.age = age
        self.gender = gender
    
    def hello_people(self):
        print(f'''Привет, {self.name}!''')


class Male(People):
    """
        Наследование класса People
    """
    
    def __init__(self, name, age) -> None:
        super().__init__(
            name=name,
            age=age,
            gender='Male'
        )
        

people_maks = People(
    name='Maks',
    age=27,
    gender='Male'
)

people_maks.hello_people()


maks = Male(
    name='Maks',
    age=27
)

maks.hello_people()