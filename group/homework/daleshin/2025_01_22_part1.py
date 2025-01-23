

# oper = ['+', '-', '*', '/', '%', '//']
# for i in oper:
    #print(f'{digit1} {oper[i]} {digit2} = {digit1 тут не прилумал как заставить из списка вытягивать операции oper[i] digit2}')

digit1 = int(input('Введите число 1: '))
digit2 = int(input('Введите число 2: '))
oper = ['+', '-', '*', '/', '%', '//']

for op in oper:
    if op == '+':
        result = digit1 + digit2
    elif op == '-':
        result = digit1 - digit2
    elif op == '*':
        result = digit1 * digit2
    elif op == '/':
        result = "Ошибка: деление на ноль" if digit2 == 0 else digit1 / digit2
    elif op == '%':
        result = "Ошибка: деление на ноль" if digit2 == 0 else digit1 % digit2
    elif op == '//':
        result = "Ошибка: деление на ноль" if digit2 == 0 else digit1 // digit2
    
    print(f'{digit1} {op} {digit2} = {result}')