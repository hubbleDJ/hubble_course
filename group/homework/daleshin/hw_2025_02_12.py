"""Homework 2025-02-12"""
# Написать рекурсивную функцию по вычислению факториала

number: int = int(input("Введите число: "))

def find_factorial(number: int|float) -> int|float:
    """Ищет факториал, в случае ошибки - вернет - 1"""

    if number < 1 or int(number) != number:
        return -1

    if number == 1 or number == 0:
        return 1

    return number * find_factorial(number - 1)

print(find_factorial(number))