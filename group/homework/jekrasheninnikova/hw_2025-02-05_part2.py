# Написать функцию, которая возвращает максимальное значение в списке
# Написать функцию, которая возвращает минимальное значение в списке
# Написать функцию, которая возвращает все четные элементы списка в виде новго списка

def min_func(nums: list[int|float]) -> int:
    """Функция, которая возвращает минимальное значение в списке"""
    minim = 10000
    for num in range(len(nums)):
        if minim > nums[num]:
            minim = nums[num]

    return minim

def max_func(nums: list[int|float]) -> int:
    """Функция, которая возвращает максимальное значение в списке"""
    maxim = -10000
    for num in range(len(nums)):
        if maxim < nums[num]:
            maxim = nums[num]

    return maxim

def even_func(nums: list[int|float]) -> int:
    """Функция, которая возвращает все четные элементы списка в виде новго списка"""
    even_list: list = []
    for num in range(len(nums)):
        if nums[num]%2==0:
            even_list.append(nums[num])

    return even_list

my_list: list = [3, 5, 10, 12, 32, 0, -4, 4, 564564, 5]

print(min_func(my_list))
print(max_func(my_list))
print(even_func(my_list))
