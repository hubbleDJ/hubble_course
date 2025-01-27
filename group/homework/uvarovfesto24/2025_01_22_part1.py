x: int = input("x= ")
y: int = input("y= ")

    #Правильный вариант
print(str(x)+ ' + '+ str(y), ' = ', int(x)+int(y))
print(f'{x} - {y} = {int(x)-int(y)}')
print('{} * {} = {}'.format(x, y, int(x)*int(y)))
print(str(x)+ ' / '+ str(y), ' = ', int(x)/int(y))
print(str(x)+ ' % '+ str(y), ' = ', int(x)%int(y))
print(str(x)+ ' // '+ str(y), ' = ', int(x)//int(y))






