# Функции

import asyncio


def PlusTwo(num):
    print(num + 2)

# PlusTwo(78)
# PlusTwo(19)
# PlusTwo(89)



def PlusTwo(num: int|float) -> None:
    print(num + 2)
    
def PlusTwo(num: int|float) -> int|float:
    """Прибавляет 2"""
    
    return num + 2


# print(PlusTwo(890))


def GenerateHelloForList(names: list[str]) -> None:
    """"""
    
    for name in names:
        print(f'Hello, {name}!')
        
GenerateHelloForList(['Den', 'Max', 'Vlad'])


def Sum(x: int|float, y: int|float) -> int|float:
    """Суммирует 2 значения"""
    
    return x + y

print(Sum(567, 687))

def SumTwoLists(one_list: list[int|float], two_list: list[int|float]) -> list[int|float]:
    """"""
    
    if len(one_list) != len(two_list):
        return []
    
    answer_list: list[int|float] = []
    
    for index in range(len(one_list)):
        answer_list.append(one_list[index] + two_list[index])
        
    return answer_list


print(SumTwoLists(
    one_list=[1, 2, 3, 4, 5],
    two_list=[9, 3, 5, 6, 8]
))

my_list: list[int] = [1, 3, 4]

def SumList() -> int:
    """"""
    
    sum_list = 0
    
    for num in my_list:
        sum_list += num
    
    return sum_list

print(SumList())


num: int = 768

def SumMyInt() -> None:
    """"""
    
    global num
    num += 1

SumMyInt()
print(num)

DIR = 'c/users'


def MyGenerator():
    """"""
    
    for i in range(100):
        yield i


for num in MyGenerator():
    print(num)


def SumInt(x: int=0, y: int=0) -> int:
    """"""
    
    return x + y

print(SumInt(y=8))


async def MyFunc() -> None:
    pass

asyncio.run(MyFunc())


def SumInt(x: int=0, y: int=0) -> int:
    """
        x: Первый аргумент
        y: Второй аргумент
        
        return: Сумма
    """
    
    return x + y


SumInt = lambda x, y: x + y

print(SumInt(1, 3))


def NewSum():
    return lol + ol

# print(NewSum())

print(max([2, 5]))
