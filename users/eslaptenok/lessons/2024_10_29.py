# Инкапсуляция
# Абстрация
# Полиморфизм
# Наследование

from accessify import private, protected

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