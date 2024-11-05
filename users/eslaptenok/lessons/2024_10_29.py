# Инкапсуляция
# Абстрация
# Полиморфизм
# Наследование

from accessify import private, protected
import json

class Car:
    """
    
    """
    
    def __init__(self, marka: str, model: str):
        self.__marka = marka
        self.__model = model
    
    def get_marka(self) -> str:
        return self.__marka
    
    def get_model(self) -> str:
        return self.__model
    
    def set_model(self, new_model) -> None:
        self.__model = new_model
    
    def my_sum(self, x, y):
        return x + y
    
        
one_car = Car('Lada', 'Vesta')
print(one_car.get_marka())

one_car.set_model('Mark 2')
print(one_car.get_model())


class RedCar:
    COLORS = (1, 255)
    
    @classmethod
    def proverca_red(cls, red_int: int) -> bool:
        """"""
        
        return cls.COLORS[0] <= red_int <= cls.COLORS[1]
    
    @private
    @staticmethod
    def my_sum(x: int, y: int) -> int:
        return x + y
    
    def __init__(self, color_rbg: tuple[int, int, int]):
        if not self.proverca_red(color_rbg[0]):
            raise Exception('Машина не красная')
    

my_car = RedCar((255, 0, 0))

# Car.my_sum(1, 2)

# RedCar.my_sum(1, 2)

try:
    a = 1
    a += 1
    100 / 0
except ZeroDivisionError as err:
    print(err)
except Exception as error:
    print(error)


[
    {
        'name': 'Visa',
        'num': '*123184'
    }, {
        'name': 'Visa',
        'num': '*123184'
    },
    ...
    ,
    {}
, ]
print('End')


age = 20
name = 'Вася' if age < 30 else 'Василий'

chet_list = []
for i in range(1, 101):
    if i % 2 == 0:
        chet_list.append(i)
        
chet_list = [i for i in range(101) if i % 2 == 0]
primer_dict = {str(i): i for i in range(100)}

print(chet_list)
print(primer_dict)

def my_func(lol: str, *args, **kwargs):
    print(lol, args, kwargs)

print(my_func('123', 132, '', o=12, iu='23'))
print(my_func(lol='12'))

with open('/Users/mvstrometskiy/home_programs/hubble_course/users/eslaptenok/lessons/2024_10_29.json', 'r') as f:
    print(json.load(f))


import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

# Объект бота
bot = Bot(token="8068611166:AAGBGSSa7Pyi4rMnGOLq6ZJISf-waYeu5QI")

# Диспетчер
dp = Dispatcher()

@dp.message()
async def cmd_start(message: types.Message):
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton('LOL'))
    await message.answer(f"Hello, {message.chat.username}!", reply_markup=markup)

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

# if __name__ == "__main__":
    # asyncio.run(main())
    
    
import sqlite3
with sqlite3.connect('my_database.db') as connection:
    cursor = connection.cursor()
    print(cursor.execute('''
        CREATE TABLE if not exists texts (
            id Int,
            scenario_id Int,
            text String
        )
    '''))
    
    print(cursor.execute('''
        insert into texts (id, scenario_id, text)
        values(0, 0, 'Привет! Это тестовое сообщение')
    '''))