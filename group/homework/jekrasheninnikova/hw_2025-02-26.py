""" hw_2025-02-26
Создать любой класс с минимум тремя свойствами и тремя методами
Создать новый класс на основе предыдущего
Добавить в новый класс несколько новых методов и свойств
"""

from time import sleep

class Doll:
    def __init__(self, id:str, name:None, year_of_production:int, mark:str, hair:str, eyes:str, color_dress:str, cost:int) -> None:
        """Инициализация переменной"""

        self.id = id
        if name != None:
            self.name = name
        self.year_of_production = year_of_production
        self.mark = mark
        self.hair = hair
        self.eyes = eyes
        self.color_dress = color_dress

        self.cost = cost

    def get_info(self) -> None:
        """Информация о кукле"""
        
        answer = input(f'Какую информацию Выхотели бы получить? [Полную/Основную] ')
        if answer == 'Полную':
            print(f'id: {self.id}\nИмя: {self.name}\n'
                  f'Год производства: {self.year_of_production}\nБренд: {self.mark}\n'
                  f'Цвет волос: {self.hair}\nЦвет глаз: {self.eyes}\nЦвет платья: {self.color_dress}')
        else:
            print(f"Имя: {self.name}\nБренд: {self.mark}\nГод выпуска: {self.year_of_production}")

    
    def buy_doll(self,wallet: int) -> int:
        """Оценка возможности приобретения куклы и, непосредственно, ее покупка"""
        
        answer = input(f'На данный момент на вашем счету {wallet} рублей. Приобрести? [y/n] ')
        if answer == 'y':
            while wallet < self.cost:
                print("Недостаточно средств для покупки куклы"
                      f" {self.mark} c именем {self.name}. Не хватает {self.cost - wallet} "
                      "рублей. Пополните счёт.")
                cash = int(input())
                wallet += cash
                answer = input(f'На данный момент на вашем счету {wallet} рублей. Приобрести? [y/n] ')
            
            if wallet >= self.cost:
                print(f'Поздравляем с приобретенной куклой {self.mark} c именем {self.name}!')
                wallet -= self.cost
                print(f'Ваш остаток {wallet} рублей')
        else:
            pass
        return wallet
    
    def play(self):
        print('Играем с куклой...')
        sleep(4)
        print('Вы поиграли с куклой Barbie')

class Barbie(Doll):
    """Класс, наследуемый от класса Doll"""
    
    def __init__(self, id, year_of_production, color_dress, cost, accessory: None):
        super().__init__(
            id = id,
            name = 'Barbie',
            year_of_production = year_of_production,
            mark = 'Barbie',
            hair = 'blond',
            eyes = 'blue',
            color_dress = color_dress, 
            cost = cost)
        
        if accessory != None:
            self.accessory = accessory
        
        
    def brush_hair(self):
        print('Расчесываем волосы...')
        sleep(4)
        print('Волосы успешно расчесаны')

    def dress(self):
        self.accessory = input('Какой аксессуар вы хотите одеть кукле? ')
        print(f'{self.accessory} был(а)/и успешно одет(а)/ы')

if __name__ == '__main__':
    
    wallet = 2000

    doll_1: Doll = Doll('01', 'Martha',2004, 'Bratz', 'grey', 'blue', 'red', 1500)
    doll_1.get_info()
    wallet = doll_1.buy_doll(wallet)


    doll_2: Doll = Doll('02', 'Karine', 1999, 'Barbie', 'blond', 'green', 'blue', 1200)
    doll_2.get_info()
    wallet = doll_2.buy_doll(wallet)

    doll_3 = Barbie('03', 2001, 'pink', 50000, ' - ')
    doll_3.get_info()
    wallet = doll_3.buy_doll(wallet)
    answer = input('Вы хотите перед игрой поухаживать за куклой? [y/n] ')
    if answer == 'y':
        doll_3.brush_hair()
        doll_3.dress()
        doll_3.play()
    else:
        doll_3.play()
    
    
    
