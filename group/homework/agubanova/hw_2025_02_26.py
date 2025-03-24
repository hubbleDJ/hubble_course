"""hw_2025_02_26"""


class Worker:
    """Работники 5чки"""

    def __init__(self, first_name: str, second_name: str, birth_year: int, passport: str, citizenship: str, post: str, status: str = "Работает") -> None:
        self.first_name = first_name
        self.second_name = second_name
        self.birth_year = birth_year
        self.passport = passport
        self.citizenship = citizenship
        self.post = post
        self.status = status

    def having_a_rest(self) -> None:
        """Человек в отпуске"""
        self.status = "Отдыхает"
        print(f'{self.second_name} {self.first_name} в очередном отпуске')

    def working(self) -> None:
        """Человек работает"""
        self.status = "Работает"
        print(f'{self.second_name} {self.first_name} работает')

    def retired(self) -> None:
        """Человек уволен"""
        self.status = "Уволен"
        print(f'{self.second_name} {self.first_name} уволен')


worker1 = Worker("Иван", "Работников", 1995, "65 351254", "РФ", "Курьер", "Отдыхает")
worker2 = Worker("Петр", "Иванов", 1996, "65 254698", "РФ", "Курьер", "Работает")

worker1.working()
worker2.retired()


class Courier(Worker):
    """Курьеры 5чки"""

    def __init__(self, first_name: str, second_name: str, birth_year: int, passport: str, citizenship: str, status: str, progress: str) -> None:
        super().__init__(first_name, second_name, birth_year, passport, citizenship, "Курьер", status)
        self.progress = progress

    def in_order(self) -> None:
        """Курьер на заказе"""
        self.progress = "Везет заказ"
        print(f'{self.second_name} {self.first_name} {self.progress}')

    def waiting(self) -> None:
        """Курьер ждет следующий заказ"""
        self.progress = "В ожидании заказа"
        print(f'{self.second_name} {self.first_name} {self.progress}')


courier1 = Courier("Дмитрий", "Греф", 1989, "17 256975", "Казахстан", "Работает", "Готов к приему заказа")

courier1.in_order()
courier1.waiting()