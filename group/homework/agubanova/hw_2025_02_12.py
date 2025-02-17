# Написать рекурсивную функцию по вычислению факториала

def find_factorial(num: int|float) -> int:
    """Считает факториал,  
    в случае ошибки - вернет - 1"""

    if num < 1 or int(num) != num:
        return -1

    if num == 0 or num == 1:
        return 1

    return num * find_factorial(num - 1)

    
# Необязательно: написать любую сортировку в которой есть рекурсия(быстрая, сортировка делением)

print(find_factorial(5.0))