number1 = int(input('Введите число 1: '))
number2 = int(input('Введите число 2: '))
znak = ['+', '-', '*', '/', '%', '//']

for op in znak:
    if op == '+':
        result = number1 + number2
    elif op == '-':
        result = number1 - number2
    elif op == '*':
        result = number1 * number2
    elif op == '/':
        result = "Ошибка: деление на ноль" if number2 == 0 else number1 / number2
    elif op == '%':
        result = "Ошибка: деление на ноль" if number2 == 0 else number1 % number2
    elif op == '//':
        result = "Ошибка: деление на ноль" if number2 == 0 else number1 // number2
    
    print(f'{number1} {op} {number2} = {result}')