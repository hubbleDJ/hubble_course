"""Module homework 2025-02-12 Recursive function factorial"""

def factorial_recursive(n: int|float) -> int|float:
    """
       Вычисляет факториал переданного числа
       в случае ошибки возвращает -1 
    """

    result = -1
    try:
        if isinstance(n, (float, int)) and n >= 0 and n == int(n):
            if n in (0, 1):
                return 1
            return n * factorial_recursive(n - 1)
    except Exception as error:
        print(error)

    return result

print(factorial_recursive(5))
print(factorial_recursive(5.0))
print(factorial_recursive("5.0"))
