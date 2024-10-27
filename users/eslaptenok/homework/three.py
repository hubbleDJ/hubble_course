# Написать рекурсивную функцию факториала
def factorial(num: int) -> int:
    """Подсчет факториала с помощью рекурсии"""

    if num == 0 or num == 1:
        return 1
    elif num < 0:
        return 'the number must not be negative'
    return factorial(num - 1) * num

print(factorial(5))
print(factorial(-2))
print(factorial(0))
print(factorial(1))
print(factorial(2))
print(factorial(6))