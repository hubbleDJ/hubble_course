"""Module homework 2025-02-12 Recursive function factorial"""

def factorial_recursive(n: int|float) -> int:
    """
       Вычисляет факториал переданного числа
       в случае ошибки возвращает -1 
    """

    result = -1
    try:
        if n.is_integer() and n >= 0:
            n = int(n)
            if n in (0, 1):
                return 1
            return n * factorial_recursive(n - 1)
    except AttributeError:
        pass

    return result

print(factorial_recursive(5))
print(factorial_recursive(5.0))
print(factorial_recursive("5.0"))
