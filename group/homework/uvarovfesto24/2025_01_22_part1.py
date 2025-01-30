x: str = input("x= ")
y: str = input("y= ")

    #Правильный вариант
print(x + ' + ' + y , ' = ', int(x)+int(y))
print(f'{x} - {y} = {int(x)-int(y)}')
print('{} * {} = {}'.format(x, y, int(x)*int(y)))
print(x + ' / ' + y, ' = ', int(x)/int(y))
print(x + ' % ' + y, ' = ', int(x)%int(y))
print(x + ' // '+ y, ' = ', int(x)//int(y))