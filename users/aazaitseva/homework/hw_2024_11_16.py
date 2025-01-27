def factorial(n: int) -> int:
    """вычисляет факториал числа."""

    if n in [0, 1]:
        return 1
    elif n < 0:
        return 0
    else:
        return n * factorial(n-1)


n = int(input('Ввод числа:'))
print(factorial(n))
