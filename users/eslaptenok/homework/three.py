# Написать рекурсивную функцию факториала
def factorial(num: int) -> int:
    """Подсчет факториала с помощью рекурсии"""

    if num in [0, 1]:
        return 1
    elif num < 0:
        return -1
    return factorial(num - 1) * num

print(factorial(5))
