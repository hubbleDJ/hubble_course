import pandas as pd
from time import sleep
from datetime import *

class Cars:
    """Класс машины"""

    def __init__(self, color: str, marka: str, model: str, type: str, year: int=None) -> None:
        self.color = color
        self.marka = marka
        self.model = model
        self.type = type
        
        if year: self.year = year
        
        self.drive_count = 0
        
        self.in_shop()
    
    def drive(self) -> None:
        """Езда машины"""
        
        print(f'{self.marka} {self.model} поехала')
        
        self.drive_count += 1
    
    def in_shop(self) -> None:
        """Сообщает об успешной покупке машины"""
        
        print(f'Поздравляю! Вы успешно купили {self.marka} {self.model} в {self.color} цвете!')


class BMW(Cars):
    """"""
    
    def __init__(self, color, model, type):
        super().__init__(
            color=color,
            marka='BMW',
            model=model,
            type=type
        )
        
    def drift(self) -> None:
        """"""
        
        print('Валим боком')
        

if __name__ == '__main__':
    car1: Cars = Cars('red', 'BMW', 'M3', 'Седан')
    my_car = Cars('red', 'BMW', 'M5', 'Седан')

    my_car.drive()
    my_car.drive()
    my_car.drive()
    print(my_car.drive_count)
    car1.drive_count
    
    my_car2 = BMW('black', 'X5', 'Кроссовер')
    my_car2.drift()
    
    print(car1.marka, car1.model)
    pd.DataFrame()
    
    print(6)
    # sleep(5)
    print(1)
    # timedelta()

    num: int = 1

    print({
        '1': 1,
        '2': []
    }.keys())


    people_one: dict = {
        'name': 'Maks',
        'age': 27
    }
