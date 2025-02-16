# Написать рекурсивную функцию по вычислению факториала
# Необязательно: написать любую сортировку,
# в которой есть рекурсия(быстрая, сортировка делением)

def factorial(num, current_factor=1):
    """factorial calculation"""
    if current_factor > num:
        return 1
    return current_factor * factorial(num, current_factor + 1)


print(factorial(int(input("Please enter your number: "))))


