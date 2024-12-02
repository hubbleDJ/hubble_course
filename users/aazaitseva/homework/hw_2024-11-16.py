#написать рекурсивну. ф-ю подсчета факториала
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)
n = int(input("Ввод числа:"))
print(factorial(n))