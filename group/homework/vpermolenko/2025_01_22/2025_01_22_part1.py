#homework1

print("Введите два числа (целых или вещественных) через enter:")
input1: str = input()
input2: str = input()

try:
    varX: float = float(input1)
    varY: float = float(input2)
    
    print(f'''Сумма: {varX} + {varY} = {varX+varY}''')
    print(f'''Разность: {varX} - {varY} = {varX-varY}''')
    print(f'''Умножение: {varX} * {varY} = {varX*varY}''')
    if(varY == 0):
        print(f'''Деление: {varX} / {varY} = Бесконечность''')
        print(f'''Остаток от деления: {varX} % {varY} = Бесконечность''')
        print(f'''Деление без остатка: {varX} // {varY} = Бесконечность''')
    else:
        print(f'''Деление: {varX} / {varY} = {varX/varY}''')
        print(f'''Остаток от деления: {varX} % {varY} = {varX%varY}''')
        print(f'''Деление без остатка: {varX} // {varY} = {varX//varY}''')
except ValueError:
    print("Вы не ввели числа")