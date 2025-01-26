#homework1

print("Введите два числа (целых или вещественных) через enter:")
input1: str = input()
input2: str = input()

try:
    x: float = float(input1)
    y: float = float(input2)
    
    print(f'''Сумма: {x} + {y} = {x + y}''')
    print(f'''Разность: {x} - {y} = {x - y}''')
    print(f'''Умножение: {x} * {y} = {x * y}''')
    if y == 0:
        print(f'''Деление: {x} / {y} = Бесконечность''')
        print(f'''Остаток от деления: {x} % {y} = Бесконечность''')
        print(f'''Деление без остатка: {x} // {y} = Бесконечность''')
    else:
        print(f'''Деление: {x} / {y} = {x / y}''')
        print(f'''Остаток от деления: {x} % {y} = {x % y}''')
        print(f'''Деление без остатка: {x} // {y} = {x // y}''')
except ValueError:
    print("Вы не ввели числа")