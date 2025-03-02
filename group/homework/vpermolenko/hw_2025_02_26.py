"""Module homework 2025-02-26 Classes"""

from datetime import datetime as dt

class User:
    """Класс пользователя"""

    def __init__(self, name: str, nickname: str, age: int=None) -> None:
        self.name = name
        self.nickname = nickname
        self.age = age
        self.register_date = dt.now()
        print(f'Пользователь {self.nickname} зарегистрирован {self.register_date}')

    def text_presentation(self) -> None:
        """выводит приветственное сообщение пользователя"""

        msg: str = f'{self.nickname}: Меня зовут {self.name}.'
        if self.age:
            msg += f' Мне {self.age} годиков.'
        print(msg)

    def text_msg(self, msg: str) -> None:
        """выводит сообщение пользователя"""

        print(f'{self.nickname}: {msg}')

class Teammate(User):
    """Класс сокомандника от пользователя"""

    def __init__(self, name, nickname, age: int=None) -> None:
        super().__init__(
            name,
            nickname,
            age
        )
        self.tasks: set[str] = set([])

    def complete_task(self, task_name: str) -> None:
        """сообщение о завершении задачи"""

        if task_name in self.tasks:
            print(f'Задача {task_name} уже выполнена')
        else:
            self.tasks.add(task_name)
            print(f'Задача {task_name} выполнена')

    def text_count_completed_tasks(self) -> None:
        """сообщение о количестве завершённых задач"""

        print(f'{self.nickname} выполнил {len(self.tasks)} задач')

if __name__ == "__main__":
    user_chad: User = User("Ben", "GigaChad")
    user_vasya: User = User("Vasya", "Pupkin", 18)
    user_chad.text_presentation()
    user_vasya.text_presentation()
    user_chad.text_msg("Здарова, бандиты.")
    user_vasya.text_msg("Приветствую.")

    teammate_chad: Teammate = Teammate("Ben", "GigaChad")
    teammate_vasya: Teammate = Teammate("Vasya", "Pupkin", 18)
    teammate_chad.text_presentation()
    teammate_vasya.text_presentation()
    teammate_chad.text_msg("Здарова, бандиты.")
    teammate_vasya.text_msg("Приветствую.")
    teammate_chad.complete_task("задача1")
    teammate_chad.complete_task("задача2")
    teammate_chad.complete_task("задача1")
    teammate_chad.text_count_completed_tasks()
    teammate_vasya.text_count_completed_tasks()
