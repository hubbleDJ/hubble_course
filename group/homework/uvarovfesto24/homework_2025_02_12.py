"""Домашка по написанию факториала"""

def factorial(num: int|float) -> int|float:
    """Считаем факториал числа"""

    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

print(factorial(7))