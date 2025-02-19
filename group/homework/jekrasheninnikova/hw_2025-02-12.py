#Рекурсия факториала

def find_fact(n: int|float) -> int:
    """
        Считает факториал
        В случае ошибки вернем -1
    """

    if n < 1 or int(n) != n: 
        return -1
    
    if n == 1:
        return n
    else:
        return n * find_fact(int(n) - 1)

print(find_fact(5.0))
print(find_fact(-10))
