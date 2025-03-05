## Инкапсуляция

class User:
    def __init__(self):
        self.tasks = []

    def new_task(self):
        self.tasks.append(Task())

    class Taks:
        def __init__(self):
            pass

## Абстракция - абстрагирование

class RequestVK:
    def __init__(self):
        self.__url = 'vk.com'
        self.__params = {}

    def get_url(self) -> str:
        return self.__url

    def set_params(self, params: dict):
        self.__params = params

    def __t(self):
        print('t')


my_req = RequestVK()
my_req.__url = '5' ## НЕЛЬЗЯ!
print(my_req.get_url())

print(my_req.__url)
print('Конец файла!')


# public - Полный доступ
# protected - Доступ внутри класса и внутри дочерних классов
# private - Доступ только внутри самого класса


# from accessify import private, protected


# class Music:
#     def __init__(self):
#         pass

#     @private
#     def play(self):
#         print('Играет')

## Полиморфизм
class User:
    
    def __init__(self, user_id: int, name: str):
        self.name = name

    def hello(self, user) -> None:

        if isinstance(user, str):
            print(f'Привет {user}!')
        elif isinstance(user, int):
            pass

maks = User(1, 'Макс')
maks.hello('Макс')


## Наследование


def test(x, y, *args):
    print(x)
    print(y)
    print(args)

test(1, 2, 4, 5, 6, 7, 8, 9)

def test(x, y, **kwargs):
    print(x)
    print(y)
    print(kwargs)

test(1, 2, p=4, o=1, z=5)


def test(x, y, *args, **kwargs):
    print(x)
    print(y)
    print(args)
    print(kwargs)

test(1, 2, 4, 5, 6, 7, 8, 9, p=4, o=1, z=5)

[1, 4, 56, 6, 8]


def get_num_symbol(symbol: str) -> int:
    symbols = {
        'a': 1,
        'b': 2,
        'c': 3
    }
    
    return symbols[symbol]
