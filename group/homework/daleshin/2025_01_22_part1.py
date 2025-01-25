digit1: int = int(input('Введите число 1: '))
digit2: int = int(input('Введите число 2: '))

print(f'{digit1} + {digit2} = {digit1 + digit2}')
print(f'{digit1} - {digit2} = {digit1 - digit2}')
print(f'{digit1} * {digit2} = {digit1 * digit2}')
if digit2 == 0 :
    print('На ноль делать нельзя')
else:
    print(f'{digit1} / {digit2} = {digit1 / digit2}') # тут нужна проверка на то что делим не на 0
    print(f'{digit1} % {digit2} = {digit1 % digit2}') # тут нужна проверка на то что делим не на 0
    print(f'{digit1} // {digit2} = {digit1 // digit2}') # тут нужна проверка на то что делим не на 0

# oper = ['+', '-', '*', '/', '%', '//']
# for i in oper:
    #print(f'{digit1} {oper[i]} {digit2} = {digit1 тут не прилумал как заставить из списка вытягивать операции oper[i] digit2}')
