if (1 == 2 and 3 < 5) or 5 == 7:
    print('ghbdtn')
elif 5 > 2:
    pass
else:
    print('hello')

var_list = [4, 985, 150]
if 2 not in var_list:
    var_list.append(2)
print(var_list)

if len('') == 0:
    print(True)

increment = 0
while increment < 100:
    print(increment)
    increment = increment + 1

min_value = 0
no_max_value = 100
step = 1
print(range(min_value, no_max_value, step))

# Проходится по всем эл. коллекции и помещает каждое ее значение в переменную
for value in var_list:
    print(value)

for symbol in 'Hello':
    print(symbol)
