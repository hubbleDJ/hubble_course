def new_sum(x: int, y: int) -> int:
    """суммирует числа"""

    return x + y

print(new_sum(1, 5))

def count_letter(text: str) -> dict[str,int]:
    res = {}    
    for letter in text:
        if letter in res:
            res[letter] += 1
        else:
            res[letter] = 1          
    return res
print(count_letter("jhyfy"))

inc = 0
def add_inc():
    global inc
    inc += 1
    return inc
print(add_inc())
print(inc)

def summa() -> int:
    """сумма чисел"""

    x = int(input("first number"))
    y = int(input("second number"))
    return x + y
numb = summa()
print(numb)

