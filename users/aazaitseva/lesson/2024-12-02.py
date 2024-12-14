from accessify import private, protected
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


# 2024-12-14
class Car:
    """Класс машины"""
    
    def __init__(self, marka: str, vladelec: str):
        self.__marka = marka
        self._vladelec = vladelec
    
    def run(self, speed: float):
        if self.motor():
            print(f'Машина поехала {speed} км в час')
        
    def getMarka(self) -> str:
        return self.__marka
    
    def setVladelec(self, new_vladelec: str) -> None:
        self._vladelec = new_vladelec
        
    def getVladelec(self) -> str:
        return self._vladelec
    
    @protected
    def motor(self) -> bool:
        return True



car_1 = Car(marka='BMW', vladelec='Maks')
print(car_1.getMarka())
print(car_1.getVladelec())
car_1.setVladelec('Nastya')
print(car_1.getVladelec())
# car_1.run(60.9)


# Инкапсуляция
# Private:
    # __name - доступен только внутри класса
    # from accessify import private
# Protected:
    # _name - доступен только внутри класса и в дочерних классах
    # from accessify import protected
    
# Полиморфизм
# Наследование
# Абстракция

class Mebel:
    
    def __init__(self):
        pass
    
    # @private
    def sobrat(self) -> None:
        print('Собран')
        
stul = Mebel()
stul.sobrat()


def getNameForId(id: int) -> str:
    ...
    return 'valera'

class User:
    def __init__(self):
        pass
    
    def hello(self, user: int | str | dict) -> None:
        if isinstance(user, str):
            print(f'Hello, {user}')
        elif isinstance(user, int):
            print(f'Hello, {getNameForId(user)}')
        elif isinstance(user, dict) and 'id' in user:
            print(f'''Hello, {getNameForId(user['id'])}''')
        elif isinstance(user, dict) and 'name' in user:
            print(f'''Hello, {user['name']}''')


class BMW(Car):
    """
        Наследование класса Car
    """
    
    def __init__(self, vladelec) -> None:
        super().__init__(
            marka='BMW',
            vladelec=vladelec
        )
    
    def service(self) -> None:
        if self.motor():
            print('Сначала заглуши мотор')
    
car_2 = BMW(vladelec='Natya')
car_2.service()


class Sobaka:
    laps = 4
    
    def __init__(self):
        pass
    
    def run(cls):
        print(f'Бежим на всех {cls.laps} лапах')
    
sob_1 = Sobaka()
sob_1.run()

# import datetime
# from datetime import datetime
from datetime import datetime as dt

import pandas as pd

print(dt.now())

from aiogram import Bot, Dispatcher
from aiogram.types import Message
import asyncio
from aiogram.methods import DeleteWebhook


bot = Bot('7695535894:AAHJN0trkCMy2adp-du1jKeIO08ar-7oqmE')
dp = Dispatcher()

@dp.message()
async def cmd_start(message: Message, bot):
    if message.text in ['/start', 'start']:
        await bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}! Как дела?')
    else:
        await bot.send_message(message.chat.id, f'Круто! И у меня тоже')
        await bot.send_photo(
            chat_id=message.chat.id,
            photo='AgACAgIAAxkBAAMOZ12cIo2m1qwG8uMzb5YctHe57mIAAq_jMRsxN_BKuekc6zJy8bcBAAMCAAN4AAM2BA'
        )
        
# Запуск процесса поллинга новых апдейтов
async def main():
    # await bot(DeleteWebhook(drop_pending_updates=True))  # отключаем обновления
    await dp.start_polling(bot, skip_updates=True)
    
if __name__ == "__main__":
    asyncio.run(main())